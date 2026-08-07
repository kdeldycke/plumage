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

"""Checks on the Bootstrap classes applied to generated pages after the build."""

from __future__ import annotations

import pytest
from pyquery import PyQuery as pq

from plumage.dom_transforms import transform


@pytest.fixture
def transformed(tmp_path):
    """Run a page fragment through the post-generation rewrite, as Pelican does."""

    def _transformed(body: str) -> pq:
        page = tmp_path / "index.html"
        page.write_text(
            f"<html><body><main id='content'>{body}</main></body></html>",
        )
        transform(str(page), context={})
        return pq(filename=str(page))

    return _transformed


def test_tables_get_bootstrap_classes(transformed):
    doc = transformed("<table><thead><tr><th>Header</th></tr></thead></table>")
    assert doc("table").has_class("table")
    assert doc("table").has_class("table-hover")
    assert doc("table thead th").attr("scope") == "col"


def test_content_images_are_responsive(transformed):
    doc = transformed("<img src='photo.png' />")
    assert doc("img").has_class("img-fluid")


@pytest.mark.parametrize("skipped", ["card-img-top", "link-icon"])
def test_card_and_link_images_are_left_alone(transformed, skipped):
    """Project cards and link favicons carry their own sizing."""
    doc = transformed(f"<img class='{skipped}' src='photo.png' />")
    assert not doc("img").has_class("img-fluid")


def test_blockquotes_are_styled(transformed):
    doc = transformed("<blockquote><p>Quoted</p></blockquote>")
    assert doc("blockquote").has_class("blockquote")
    assert doc("blockquote p").has_class("p-2")


def test_code_blocks_are_styled(transformed):
    assert transformed("<div class='highlight'>code</div>")(".highlight").has_class(
        "rounded"
    )


# Python Markdown's admonition types, mapped onto Bootstrap's alert variants.
ADMONITION_CASES = (
    ("note", "alert-info"),
    ("tip", "alert-info"),
    ("warning", "alert-warning"),
    ("caution", "alert-warning"),
    ("error", "alert-danger"),
    ("danger", "alert-danger"),
)


@pytest.mark.parametrize(("admonition", "alert"), ADMONITION_CASES)
def test_admonitions_become_alerts(transformed, admonition, alert):
    doc = transformed(
        f"<div class='admonition {admonition}'>"
        "<p class='admonition-title'>Title</p><p>Body</p></div>",
    )
    assert doc(".admonition").has_class("alert")
    assert doc(".admonition").has_class(alert)
    assert doc(".admonition").attr("role") == "alert"
    assert doc(".admonition-title").has_class("alert-heading")
