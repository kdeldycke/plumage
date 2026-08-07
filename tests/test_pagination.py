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

"""Checks on the link relations the paginator advertises to crawlers."""

from __future__ import annotations

from dataclasses import dataclass, field

import pytest


@dataclass
class FakePage:
    """Stand-in for Pelican's Page object, reduced to what the template reads."""

    number: int
    total: int
    url: str = field(init=False)

    def __post_init__(self):
        self.url = f"page/{self.number}.html"

    def has_previous(self) -> bool:
        return self.number > 1

    def has_next(self) -> bool:
        return self.number < self.total


@dataclass
class FakePaginator:
    """Stand-in for Pelican's Paginator object."""

    num_pages: int

    @property
    def page_range(self) -> range:
        return range(1, self.num_pages + 1)

    def page(self, number: int) -> FakePage:
        return FakePage(number, self.num_pages)


@pytest.fixture
def paginate(render):
    """Render pagination.html positioned on a given page of a 7-page archive."""

    def _paginate(current: int, total: int = 7):
        page = FakePage(current, total)
        doc = render(
            "pagination.html",
            DEFAULT_PAGINATION=True,
            articles_page=page,
            articles_paginator=FakePaginator(total),
            articles_previous_page=FakePage(max(current - 1, 1), total),
            articles_next_page=FakePage(min(current + 1, total), total),
        )
        # Numbered page links only: the prev/next arrows are separate, static markup.
        return [a for a in doc("a.page-link") if a.text and a.text.strip().isdigit()]

    return _paginate


def test_numbered_links_are_rendered(paginate):
    assert paginate(4)


def test_no_whitespace_only_rel(paginate):
    """A page with no relation must omit rel, not emit a blank one.

    The attribute used to be assembled inline from four conditionals, so an interior page
    matching none of them rendered rel="    ": whitespace only, and meaningless to crawlers.
    """
    for link in paginate(4):
        rel = link.get("rel")
        assert rel is None or rel.strip() == rel != ""


@pytest.mark.parametrize(
    ("current", "number", "expected"),
    [
        # Page 1 of 7 is both the first page and the one before page 2.
        (2, 1, "first prev"),
        (1, 1, "first"),
        (1, 2, "next"),
        (1, 7, "last"),
        (6, 7, "last next"),
        (4, 3, "prev"),
        (4, 5, "next"),
    ],
)
def test_rel_values(paginate, current, number, expected):
    links = {int(a.text.strip()): a.get("rel") for a in paginate(current)}
    assert links[number] == expected
