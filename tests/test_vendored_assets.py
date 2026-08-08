# Copyright Kevin Deldycke <kevin@deldycke.com> and contributors.
#
# This program is Free Software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.

"""Checks tying the assets copied out of npm packages to the markup asking for them.

Each of these is committed under `static/`, because `node_modules` never reaches the
distribution, and refreshed by the `sync-vendored-assets` job from the release pinned in
`package.json`. Two halves therefore move separately: Dependabot bumps the version, the
job replaces the file. These cover the seam between them, and the one before it, where a
template or stylesheet names a file nobody ships.
"""

from __future__ import annotations

import json
import re
from pathlib import Path

import pytest

from plumage import PLUMAGE_ROOT

STATIC = PLUMAGE_ROOT / "static"
TEMPLATES = PLUMAGE_ROOT / "templates"

MAIN_SCSS = (STATIC / "css" / "main.scss").read_text()

FONT_DIR_URL = "/theme/fonts"
"""Where the theme serves its fonts from, once Pelican has copied `static/` to `theme/`."""

FONT_FILES = re.findall(r"url\('#\{\$bootstrap-icons-font-dir\}/([^']+)'\)", MAIN_SCSS)
"""Every font `main.scss` points an `@font-face` at, read off the source.

Matched in the source rather than in compiled CSS on purpose: compiling `main.scss` pulls
in Bootstrap from `node_modules`, and the suite is meant to run without the npm toolchain.
"""

SCRIPT_FILES = sorted({
    name
    for template in TEMPLATES.glob("*.html")
    for name in re.findall(
        r'<script src="\{\{ SITEURL \}\}/theme/js/([^"]+)"', template.read_text()
    )
})
"""Every script the templates load from the theme itself, vendored or not."""

VENDORED = {
    "bootstrap.bundle.min.js": "bootstrap/dist/js/bootstrap.bundle.min.js",
    "masonry.pkgd.min.js": "masonry-layout/dist/masonry.pkgd.min.js",
    "bootstrap-icons.woff2": "bootstrap-icons/font/fonts/bootstrap-icons.woff2",
}
"""Each copied asset, against its path inside `node_modules`."""


def test_stylesheet_asks_for_a_font():
    assert FONT_FILES


def test_fonts_are_served_from_the_theme_directory():
    """The interpolated URLs above are only right if the directory is this one."""
    assert f"$bootstrap-icons-font-dir: '{FONT_DIR_URL}';" in MAIN_SCSS


def test_every_font_asked_for_is_shipped():
    """A missing file here costs every icon on the site, and nothing else fails."""
    for name in FONT_FILES:
        assert (STATIC / "fonts" / name).is_file()


def test_no_font_is_shipped_unused():
    shipped = {p.name for p in (STATIC / "fonts").iterdir() if p.is_file()}
    assert shipped == set(FONT_FILES)


def test_every_script_asked_for_is_shipped():
    assert SCRIPT_FILES
    for name in SCRIPT_FILES:
        assert (STATIC / "js" / name).is_file()


def test_no_script_is_shipped_unused():
    shipped = {p.name for p in (STATIC / "js").iterdir() if p.is_file()}
    assert shipped == set(SCRIPT_FILES)


def test_no_asset_is_loaded_from_a_cdn():
    """Anything served from a URL carries a version no tooling can see or bump."""
    for template in TEMPLATES.glob("*.html"):
        markup = template.read_text()
        for host in ("cdnjs.cloudflare.com", "cdn.jsdelivr.net", "unpkg.com"):
            assert host not in markup, f"{template.name} loads an asset from {host}"


@pytest.mark.parametrize("name", sorted(VENDORED))
def test_vendored_asset_is_declared_as_a_dependency(name):
    """Its version has to live in a manifest, which is the only thing Dependabot reads."""
    package = json.loads((PLUMAGE_ROOT / "package.json").read_text())
    assert VENDORED[name].split("/")[0] in package["dependencies"]


@pytest.mark.parametrize("name", sorted(VENDORED))
def test_vendored_asset_matches_the_pinned_release(name):
    """The committed copy is the file from the release `package.json` declares.

    Only checked when the npm tree is installed, which it is not in a bare checkout: the
    sync-vendored-assets job runs `npm ci` first, and that is where a mismatch matters.
    """
    upstream = PLUMAGE_ROOT / "node_modules" / Path(VENDORED[name])
    if not upstream.is_file():
        pytest.skip("npm tree not installed")

    shipped = next(p for p in STATIC.rglob(name) if p.is_file())
    assert upstream.read_bytes() == shipped.read_bytes()
