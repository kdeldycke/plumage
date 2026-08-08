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

"""Fixtures rendering the theme's templates without a full Pelican build."""

from __future__ import annotations

from collections.abc import Callable

import pelican
import pytest
from jinja2 import ChoiceLoader, DictLoader, Environment, FileSystemLoader, nodes
from jinja2.ext import Extension
from pyquery import PyQuery as pq

from plumage import PLUMAGE_ROOT, __version__

TEMPLATE_DIR = PLUMAGE_ROOT / "templates"


class StubAssetsExtension(Extension):
    """Stand-in for the ``{% assets %}`` tag of the ``pelican-webassets`` plugin.

    The real tag compiles SCSS through ``libsass`` and PostCSS, which needs the npm
    toolchain the theme installs at build time. Templates only care that the block
    renders once with an ``ASSET_URL`` bound to it, so that is all this reproduces.
    """

    # Not annotated ClassVar, as ruff would have it: Jinja declares tags as an instance
    # variable, and mypy rejects overriding one with a class variable.
    tags = {"assets"}  # noqa: RUF012

    def parse(self, parser):
        lineno = next(parser.stream).lineno
        # Discard the filters/output/source arguments: none of them reach the markup.
        while parser.stream.current.type != "block_end":
            parser.stream.skip()
        body = parser.parse_statements(("name:endassets",), drop_needle=True)
        bind_url = nodes.Assign(
            nodes.Name("ASSET_URL", "store"),
            nodes.Const("theme/css/main.min.css"),
        )
        # Scope the binding so ASSET_URL does not leak into the rest of the template.
        return nodes.Scope([bind_url, *body]).set_lineno(lineno)


BASE_CONTEXT: dict = {
    # Anything the templates iterate over has to be present: Jinja's default
    # undefined renders as an empty string but raises as soon as it is looped on.
    "categories": [],
    "dates": [],
    "draft_pages": [],
    "drafts": [],
    "hidden_articles": [],
    "hidden_pages": [],
    "MENUITEMS": [],
    "pages": [],
    # Plain values the base template expects from Pelican and from check_config(). The two
    # versions are read off the modules check_config() reads them from, rather than pinned:
    # nothing bumps a literal here, so a pinned one would go stale on the next release and
    # leave the footer asserting a version no longer shipped.
    "AUTHOR": "Test Author",
    "CODE_STYLE": "monokai",
    "DEFAULT_LANG": "en",
    "output_file": "index.html",
    "PELICAN_VERSION": pelican.__version__,
    "PLUMAGE_VERSION": __version__,
    "SITENAME": "Test Site",
    "SITEURL": "",
}
"""Smallest Pelican context that renders ``base.html`` end to end."""


@pytest.fixture(scope="session")
def jinja_env() -> Environment:
    """A Jinja environment configured the way Pelican configures a theme's own."""
    return Environment(
        loader=FileSystemLoader(TEMPLATE_DIR),
        # Mirrors Pelican's JINJA_ENVIRONMENT default. Autoescaping stays off, as
        # the templates escape explicitly with the |e filter.
        trim_blocks=True,
        lstrip_blocks=True,
        extensions=[StubAssetsExtension],
    )


@pytest.fixture
def render_source(jinja_env: Environment) -> Callable:
    """Render a template against ``BASE_CONTEXT`` and return its raw markup.

    Nothing parses the result, so an unbalanced tag survives to be asserted on. The
    ``render`` fixture below cannot see one: a parser repairs the markup on the way in.
    """

    def _render_source(template: str = "base.html", **overrides) -> str:
        return jinja_env.get_template(template).render(BASE_CONTEXT | overrides)

    return _render_source


@pytest.fixture
def render(render_source: Callable) -> Callable:
    """Render a template against ``BASE_CONTEXT`` and return the parsed document."""

    def _render(template: str = "base.html", **overrides) -> pq:
        return pq(render_source(template, **overrides))

    return _render


@pytest.fixture
def render_override(jinja_env: Environment) -> Callable:
    """Render a template through a child replacing one of its blocks.

    Stands in for a downstream theme extending Plumage, which is the only thing a named
    block is worth anything for. What it checks is that the override reaches the output
    and the default content it displaces does not.
    """

    def _render_override(
        block: str, markup: str, template: str = "base.html", **overrides
    ) -> pq:
        child = (
            f"{{% extends '{template}' %}}"
            f"{{% block {block} %}}{markup}{{% endblock {block} %}}"
        )
        env = jinja_env.overlay(
            loader=ChoiceLoader(
                [DictLoader({"child.html": child}), FileSystemLoader(TEMPLATE_DIR)],
            ),
        )
        return pq(env.get_template("child.html").render(BASE_CONTEXT | overrides))

    return _render_override
