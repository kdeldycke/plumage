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

import os
import subprocess
import sys

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
            encoding="utf-8",
        )
        transform(str(page), context={})
        return pq(filename=str(page), encoding="utf-8")

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


# The admonition types the MyST and reStructuredText readers emit, mapped onto
# Bootstrap's alert variants.
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


NON_ASCII = "Café Ünicode 日本語"
"""Characters a site picks up from an author name, a quote or a title."""


def test_non_ascii_content_survives_the_rewrite(transformed):
    assert NON_ASCII in transformed(f"<p>{NON_ASCII}</p>")("p").text()


ASCII_LOCALE = {
    # An ASCII locale, standing in for the cp1252 one a Windows console hands Python.
    # PEP 538 would coerce C to C.UTF-8 and PEP 540's UTF-8 mode would bypass the locale
    # altogether, so both have to be off to reach it on a POSIX runner.
    "LC_ALL": "C",
    "PYTHONCOERCECLOCALE": "0",
    "PYTHONUTF8": "0",
}


def test_rewrite_is_utf8_whatever_the_platform_default_is(tmp_path):
    """Neither end of the round-trip may fall back to the platform's encoding.

    ``transform()`` re-reads and overwrites a page Pelican wrote as UTF-8. Name no
    encoding on either side and Python takes the locale's: cp1252 on Windows, which
    raises on the first accented character anywhere in a site, and this is a theme
    people build on their own machines. A POSIX runner defaults to UTF-8 and so cannot
    reproduce it in-process, hence the subprocess in an ASCII locale.
    """
    page = tmp_path / "index.html"
    page.write_text(
        f"<html><body><main id='content'><p>{NON_ASCII}</p></main></body></html>",
        encoding="utf-8",
    )
    script = (
        "from plumage.dom_transforms import transform;"
        f" transform({str(page)!r}, context={{}})"
    )
    run = subprocess.run(
        [sys.executable, "-c", script],
        capture_output=True,
        check=False,
        env=os.environ | ASCII_LOCALE,
        text=True,
    )

    assert run.returncode == 0, run.stderr
    assert NON_ASCII in page.read_text(encoding="utf-8")
