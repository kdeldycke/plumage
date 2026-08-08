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

"""Checks tying the web fonts the theme ships to the ones its stylesheet asks for.

Nothing here compiles SCSS: the point is that the two halves of a self-hosted font agree,
one being a `url()` in a stylesheet and the other a binary in the package. They are kept in
step by two different things, Dependabot for the version and the sync-bootstrap-icons job
for the file, which is exactly the seam where they can drift apart.
"""

from __future__ import annotations

import json
import re

from plumage import PLUMAGE_ROOT

FONT_DIR = PLUMAGE_ROOT / "static" / "fonts"

MAIN_SCSS = (PLUMAGE_ROOT / "static" / "css" / "main.scss").read_text()

FONT_DIR_URL = "/theme/fonts"
"""Where the theme serves its fonts from, once Pelican has copied `static/` to `theme/`."""

FONT_URLS = re.findall(
    r"url\('#\{\$bootstrap-icons-font-dir\}/([^']+)'\)",
    MAIN_SCSS,
)
"""Every self-hosted font `main.scss` points an `@font-face` at, read off the source.

Matched in the source rather than in compiled CSS on purpose: compiling `main.scss` pulls
in Bootstrap from `node_modules`, and the suite is meant to run without the npm toolchain.
"""


def test_stylesheet_asks_for_a_font():
    assert FONT_URLS


def test_fonts_are_served_from_the_theme_directory():
    """The interpolated URLs above are only right if the directory is this one."""
    assert f"$bootstrap-icons-font-dir: '{FONT_DIR_URL}';" in MAIN_SCSS


def test_every_font_asked_for_is_shipped():
    """A missing file here costs every icon on the site, and nothing else fails."""
    for name in FONT_URLS:
        assert (FONT_DIR / name).is_file()


def test_no_font_is_shipped_unused():
    shipped = {p.name for p in FONT_DIR.iterdir() if p.is_file()}
    assert shipped == set(FONT_URLS)


def test_icon_font_is_not_loaded_from_a_cdn():
    """The font moved in-package so its version sits somewhere Dependabot can bump it."""
    base = (PLUMAGE_ROOT / "templates" / "base.html").read_text()
    assert "bootstrap-icons" not in base


def test_icon_font_matches_the_pinned_release():
    """The vendored binary comes from the release `package.json` declares.

    Only checked when the npm tree is installed, which it is not in a bare checkout: the
    sync-bootstrap-icons job runs `npm ci` first, and that is where a mismatch matters.
    """
    package = json.loads((PLUMAGE_ROOT / "package.json").read_text())
    assert "bootstrap-icons" in package["dependencies"]

    upstream = (
        PLUMAGE_ROOT
        / "node_modules"
        / "bootstrap-icons"
        / "font"
        / "fonts"
        / "bootstrap-icons.woff2"
    )
    if upstream.is_file():
        assert upstream.read_bytes() == (FONT_DIR / "bootstrap-icons.woff2").read_bytes()
