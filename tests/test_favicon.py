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

"""Checks tying the favicons the theme ships to the ones its markup asks for."""

from __future__ import annotations

import pytest

from plumage import PLUMAGE_ROOT

FAVICON_DIR = PLUMAGE_ROOT / "static" / "favicon"

ALL_FAVICONS = sorted(p.name for p in FAVICON_DIR.iterdir() if p.is_file())
"""Every favicon add_favicon_assets() copies to the root of the generated site."""


def test_favicons_are_shipped():
    assert "favicon.ico" in ALL_FAVICONS
    assert "site.webmanifest" in ALL_FAVICONS


@pytest.mark.parametrize("favicon", ALL_FAVICONS)
def test_favicon_is_a_readable_file(favicon):
    """add_favicon_assets() asserts on this, and fails the whole build if it slips."""
    asset = FAVICON_DIR / favicon
    assert asset.is_file()
    assert asset.stat().st_size


FAVICON_RELS = ("apple-touch-icon", "icon", "manifest", "mask-icon")
"""The link relations base.html uses to point at a favicon."""


def test_referenced_favicons_are_shipped(render):
    """The base template links favicons by absolute path, bypassing {static}.

    Nothing else checks those hrefs resolve, so a renamed asset would only ever
    surface as a 404 on a generated site.
    """
    doc = render()
    referenced = {
        link.get("href").lstrip("/")
        for rel in FAVICON_RELS
        for link in doc(f'head link[rel="{rel}"]')
    }
    assert referenced
    assert referenced <= set(ALL_FAVICONS)
