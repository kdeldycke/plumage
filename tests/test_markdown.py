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

"""Checks tying the MyST reader's output to the rewrites the theme performs on it.

``test_dom_transforms.py`` feeds the rewrite hand-written HTML, so it proves the
selectors work but not that anything ever emits the markup they look for. These tests
start from Markdown source and go through the reader a site's content travels through.

The reader picks between two renderers per document, and they do not agree on how a code
block is marked up, so anything touching code is exercised against both. See
``RENDERER_SOURCES`` for how each is reached.
"""

from __future__ import annotations

import pytest
from pelican.plugins.myst_reader import MySTReader
from pelican.readers import Readers, RstReader
from pelican.settings import DEFAULT_CONFIG
from pyquery import PyQuery as pq

from plumage.dom_transforms import transform

FRONTMATTER = "---\ntitle: Probe\n---\n\n"

# The reader hands a document to Sphinx when it holds an intra-site link, a bibliography
# or maths, and to docutils otherwise. Only the docutils one needs the code block fixup,
# so both paths have to stay covered.
RENDERER_SOURCES = {
    "docutils": "",
    "sphinx": "A [link]({filename}/other.md).\n\n",
}


def read_and_transform(tmp_path, reader_class, name: str, source: str) -> pq:
    """Read a content file the way Pelican does, then apply the post-generation rewrite.

    Which reader gets there is the variable: the two of them produce the code block
    markup the rewrite has to tell apart, and everything downstream of the read is the
    same page Pelican would have written out.
    """
    page = tmp_path / name
    page.write_text(source, encoding="utf-8")

    settings = DEFAULT_CONFIG.copy()
    settings["PATH"] = str(tmp_path)
    content, _metadata = reader_class(settings).read(str(page))

    html = tmp_path / "index.html"
    html.write_text(
        f"<html><body><main id='content'>{content}</main></body></html>",
        encoding="utf-8",
    )
    transform(str(html), context={})
    return pq(filename=str(html), encoding="utf-8")


@pytest.fixture
def rendered(tmp_path):
    """Read MyST the way Pelican does, then apply the post-generation rewrite."""

    def _rendered(source: str) -> pq:
        return read_and_transform(
            tmp_path, MySTReader, "index.md", FRONTMATTER + source
        )

    return _rendered


def test_myst_reader_claims_markdown_files():
    """The reader has to win `.md` from Pelican's own MarkdownReader.

    Both register for the extension. If the MyST one ever stopped taking precedence,
    directives would silently render as literal text rather than fail.
    """
    settings = DEFAULT_CONFIG.copy()
    readers = Readers(settings)
    assert isinstance(readers.readers["md"], MySTReader)


@pytest.mark.parametrize("directive", ("note", "warning", "tip", "danger"))
def test_directive_fences_become_admonitions(rendered, directive):
    """The ```{note} syntax, which is the whole reason the reader is a dependency."""
    doc = rendered(f"```{{{directive}}}\nBody text.\n```")
    assert doc(".admonition"), "directive rendered as literal text"
    assert doc(".admonition").has_class("alert")
    assert doc(".admonition").attr("role") == "alert"
    assert doc(".admonition-title").has_class("alert-heading")


def test_colon_fence_directives_need_opting_in(rendered):
    """The `:::{note}` spelling is inert until a site enables MyST's colon_fence.

    Pinned as a known limitation rather than a bug: nothing the theme does affects it,
    and it fails by rendering as literal text, which is easy to mistake for a theme
    problem. `readme.md` documents the setting that turns it on.
    """
    assert not rendered(":::{note}\nBody text.\n:::")(".admonition")


@pytest.mark.parametrize("prelude", RENDERER_SOURCES.values(), ids=RENDERER_SOURCES)
def test_code_blocks_are_highlighted(rendered, prelude):
    """Syntax colors must not depend on which renderer the document happened to reach.

    Every Pygments stylesheet is generated with `-a ".highlight"`, so a block that never
    lands inside that container gets no colors, however many token spans Pygments emits.
    """
    doc = rendered(f'{prelude}```python\nprint("hello")\n```')

    highlighted = doc(".highlight")
    assert highlighted, "code block never reached a .highlight container"
    # The tokens Pygments emits are only ever selected through the container.
    assert highlighted.find("span.nb"), "no Pygments token spans under .highlight"
    assert highlighted.has_class("rounded")
    assert highlighted.has_class("shadow-sm")


@pytest.mark.parametrize("prelude", RENDERER_SOURCES.values(), ids=RENDERER_SOURCES)
def test_code_blocks_are_never_nested_in_two_containers(rendered, prelude):
    """The fixup must skip blocks a renderer already wrapped."""
    doc = rendered(f'{prelude}```python\nprint("hello")\n```')
    assert not doc(".highlight .highlight")


def test_unlexed_code_blocks_still_get_a_container(rendered):
    """A fence with no language carries no token spans, but is still a code box."""
    assert rendered("```\nplain text\n```")(".highlight").has_class("rounded")


@pytest.mark.parametrize(
    ("source", "is_code_box"),
    (
        (".. code-block:: python\n\n    print(1)\n", True),
        # docutils reuses `literal-block` for `::` literals, which carry no lexer output
        # and must not be dressed up as code boxes.
        ("A paragraph::\n\n    indented literal\n", False),
    ),
    ids=("code-block", "plain-literal"),
)
def test_rst_literal_blocks_are_told_apart(tmp_path, source, is_code_box):
    """The theme serves `.rst` content too, where the two shapes are distinguishable."""
    doc = read_and_transform(
        tmp_path, RstReader, "index.rst", f":title: Probe\n\n{source}"
    )

    assert bool(doc(".highlight")) is is_code_box
    assert not doc(".highlight .highlight")


def test_tables_get_bootstrap_classes(rendered):
    doc = rendered("| a | b |\n|---|---|\n| 1 | 2 |")
    assert doc("table").has_class("table")
    assert doc("table").has_class("table-hover")
    assert doc("table thead th").attr("scope") == "col"


def test_blockquotes_are_styled(rendered):
    doc = rendered("> Quoted")
    assert doc("blockquote").has_class("blockquote")
    assert doc("blockquote p").has_class("p-2")
