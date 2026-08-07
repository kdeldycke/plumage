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

"""Checks on the month grouping the archives build by hand.

Its definition list opens inside one ``{% if %}`` and closes in two others, one per
boundary it has to detect. No linter can pair that up, so the loop sits behind a
``{# djlint:off #}`` fence where neither the linter nor the formatter looks. Rendering
the archives is what covers it instead.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date

import pytest


@dataclass
class FakeArticle:
    """Stand-in for Pelican's Article object, reduced to what the template reads."""

    date: date
    title: str
    url: str


ARTICLES = (
    FakeArticle(date(2024, 3, 15), "Ides of March", "ides.html"),
    FakeArticle(date(2024, 3, 2), "Early March", "early-march.html"),
    FakeArticle(date(2024, 1, 20), "January", "january.html"),
    FakeArticle(date(2023, 11, 5), "November", "november.html"),
)
"""Reverse-chronological, the order Pelican hands its dates to the archives.

Two articles share a month, so the grouping has to keep them in one list; the other two
each open a list of their own, one across a month boundary and one across a year.
"""

MONTHLY_ENTRY_COUNTS = [2, 1, 1]
"""Articles per rendered list, in document order: March, January, then November."""


ARCHIVE_CONTEXT = {"dates": ARTICLES, "ARCHIVES_SAVE_AS": "archives.html"}


@pytest.fixture
def archives(render):
    return render("archives.html", **ARCHIVE_CONTEXT)


@pytest.fixture
def archives_source(render_source):
    return render_source("archives.html", **ARCHIVE_CONTEXT)


def test_a_card_per_year(archives):
    assert len(archives(".accordion > .card")) == 2


def test_a_list_per_month(archives):
    assert len(archives("dl.row")) == len(MONTHLY_ENTRY_COUNTS)


def test_entries_are_grouped_by_month(archives):
    counts = [len(group.find("dd")) for group in archives("dl.row").items()]
    assert counts == MONTHLY_ENTRY_COUNTS


def test_lists_are_never_nested(archives):
    """A missing closing tag does not fail to parse: the next list opens inside it."""
    assert not archives("dl dl")


def test_lists_are_balanced_in_the_markup(archives_source):
    """The last list of a year is closed by its own branch, and nothing else closes it.

    Lose that branch and a parser quietly repairs the result, so the rendered tree still
    looks right. Only the markup shows the imbalance. This is the check H025 would make,
    were it not per-file-ignored here for misreading the conditional closing tag.
    """
    opened = archives_source.count("<dl")
    assert opened == archives_source.count("</dl>") == len(MONTHLY_ENTRY_COUNTS)


@pytest.mark.parametrize("tag", ["dt", "dd"])
def test_every_entry_sits_in_a_list(archives, tag):
    """One outside a list means the grouping emitted a boundary it should not have."""
    assert len(archives(f"dl.row {tag}")) == len(archives(tag)) == len(ARTICLES)


def test_lists_stay_inside_their_year(archives):
    """Each list closes before the card does, rather than leaking into the next year."""
    assert len(archives(".card-body > dl.row")) == len(MONTHLY_ENTRY_COUNTS)


def test_articles_are_linked(archives):
    links = {link.text(): link.attr("href") for link in archives("dd a").items()}
    assert links == {a.title: f"/{a.url}" for a in ARTICLES}


def test_entries_carry_a_machine_readable_date(archives):
    """The stamp lives in datetime, where a parser looks for it.

    ``title`` repeats it only to keep the hover tooltip the ``<abbr>`` this replaced
    used to provide.
    """
    entries = list(archives("dt time.published").items())
    assert [t.attr("datetime") for t in entries] == [
        a.date.isoformat() for a in ARTICLES
    ]
    assert [t.attr("title") for t in entries] == [a.date.isoformat() for a in ARTICLES]
