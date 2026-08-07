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

"""Checks on the project card, whose tags do not all open and close together.

The thumbnail anchor spans two separate ``{% if %}`` blocks, a shape djlint cannot
indent, so it sits behind a ``{# djlint:off #}`` fence where neither the linter nor the
formatter looks. Rendering the card is what covers it instead.
"""

from __future__ import annotations

from dataclasses import dataclass

import pytest

THUMB = "images/thumb.png"
THUMB_LINK = "https://example.com/project"


@dataclass
class FakeTag:
    """Stand-in for Pelican's Tag object, reduced to what macros.html reads."""

    name: str
    url: str


PROJECT = {
    "name": "Test Project",
    "desc": "A test project.",
    "roles": ["maintainer"],
    # Matches the tag below, so this one renders through the render_tag macro. A tool
    # with no matching tag takes the other branch, and gets a plain badge.
    "tools": ["python", "sqlite"],
    "links": ["https://github.com/example/project"],
}


@pytest.fixture
def project_card(render):
    """Render projects.html around a single project, with overridable fields."""

    def _project_card(**fields):
        return render(
            "projects.html",
            PROJECTS=[PROJECT | fields],
            tags=[(FakeTag("python", "tag/python.html"), ["an-article"])],
        )

    return _project_card


def test_card_renders(project_card):
    doc = project_card()
    assert doc(".card .card-body .card-title").text() == "Test Project"
    assert "A test project." in doc(".card .card-body").text()


def test_thumbnail_is_wrapped_in_its_link(project_card):
    doc = project_card(thumb=THUMB, thumb_link=THUMB_LINK)
    assert doc(f"a[href='{THUMB_LINK}'] img.card-img-top")


def test_thumbnail_without_a_link_carries_no_anchor(project_card):
    """Only the closing half of the anchor is conditional on anything else."""
    doc = project_card(thumb=THUMB)
    assert doc("img.card-img-top")
    assert not doc("a img.card-img-top")


def test_card_without_a_thumbnail_shows_no_image(project_card):
    doc = project_card()
    assert not doc("img.card-img-top")


@pytest.mark.parametrize(
    "fields",
    [
        {},
        {"thumb": THUMB},
        {"thumb": THUMB, "thumb_link": THUMB_LINK},
    ],
    ids=["no-thumbnail", "thumbnail", "linked-thumbnail"],
)
def test_thumbnail_anchor_never_swallows_the_card_body(project_card, fields):
    """Drop either half of the anchor and the body is parsed as part of the link.

    An unclosed <a> does not fail to parse: everything that follows is re-parented
    into it, so the whole card becomes one giant link to the thumbnail.
    """
    doc = project_card(**fields)
    assert doc(".card-body")
    assert not doc("a .card-body")


def test_badge_list_is_not_wrapped_in_a_paragraph(project_card):
    """A <ul> may not sit inside a <p>, which is what this used to be.

    The parser closes a paragraph at the list, which moves the list out of the element
    carrying card-text and leaves a stray empty paragraph behind.
    """
    doc = project_card()
    assert doc(".card-text ul.list-inline li")
    assert not doc("p ul")


def test_roles_and_tools_are_badged(project_card):
    """Every role and tool shows up, whichever of the three branches emits it."""
    badges = project_card()(".card-text ul.list-inline .badge")
    assert {badge.text().strip() for badge in badges.items()} == {
        "maintainer",
        "python",
        "sqlite",
    }
