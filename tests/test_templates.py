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

"""High-level checks on the markup the theme's templates produce."""

from __future__ import annotations

from datetime import UTC, datetime
from types import SimpleNamespace

import pytest

from plumage import PLUMAGE_ROOT

ALL_TEMPLATES = sorted(p.name for p in (PLUMAGE_ROOT / "templates").glob("*.html"))
"""Every template the theme ships. Read at import time, to parametrize with it."""


def classes(element) -> str:
    """Normalize an element's class attribute, which templates pad with spaces."""
    return " ".join((element.attr("class") or "").split())


def test_theme_ships_templates():
    assert "base.html" in ALL_TEMPLATES
    assert len(ALL_TEMPLATES) > 10


@pytest.mark.parametrize("template", ALL_TEMPLATES)
def test_template_has_valid_syntax(jinja_env, template):
    """Every shipped template parses, including the ones no test renders."""
    assert jinja_env.get_template(template)


def test_base_renders(render):
    doc = render()
    assert doc("title").text().endswith("Test Site")
    assert doc("main#content")
    assert doc("footer")


# A full-width layout drops both sidebars, so the main content always spans the
# whole row. Otherwise each declared sidebar takes 3 of the 12 columns. The block
# above the content mirrors its width, and is offset only by a left sidebar.
LAYOUT_CASES = (
    # layout, has_left, has_right, main columns, top block classes, sidebar count
    (None, False, False, "col-md-12", "col-md-12", 0),
    (None, False, True, "col-md-9", "col-md-9", 1),
    (None, True, False, "col-md-9", "col-md-9 offset-md-3", 1),
    (None, True, True, "col-md-6", "col-md-6 offset-md-3", 2),
    ("full-width", False, False, "col-md-12", "col-md-12", 0),
    ("full-width", False, True, "col-md-12", "col-md-12", 0),
    ("full-width", True, False, "col-md-12", "col-md-12", 0),
    ("full-width", True, True, "col-md-12", "col-md-12", 0),
)


@pytest.mark.parametrize(
    ("layout", "has_left", "has_right", "main_cls", "top_cls", "sidebars"),
    LAYOUT_CASES,
)
def test_layout_columns(
    render, layout, has_left, has_right, main_cls, top_cls, sidebars
):
    context = {"has_left": has_left, "has_right": has_right}
    if layout:
        context["LAYOUT"] = layout
    doc = render(**context)

    rows = doc(".container.mt-5 .row")
    assert classes(doc("main#content")) == main_cls
    assert classes(rows.eq(0).children().eq(0)) == top_cls
    assert len(rows.eq(1).children(".col-md-3")) == sidebars


@pytest.mark.parametrize("sidebar", ["LEFT_SIDEBAR", "RIGHT_SIDEBAR"])
def test_sidebar_setting_declares_content(render, sidebar):
    """Declaring a sidebar through the settings is enough to make it show up."""
    doc = render(**{sidebar: "<p>Sidebar body</p>"})
    assert len(doc(".container.mt-5 .row").eq(1).children(".col-md-3")) == 1
    assert "Sidebar body" in doc(".container.mt-5").text()


def test_full_width_layout_drops_sidebar_content(render):
    """A full-width page ignores sidebars, whatever the settings declare."""
    doc = render(LAYOUT="full-width", LEFT_SIDEBAR="<p>Sidebar body</p>")
    assert "Sidebar body" not in doc.text()


NAV_CASES = (
    # Setting turning the menu section on, context feeding it, and the name the
    # current item is compared against.
    ("DISPLAY_PAGES_ON_MENU", "pages", "page"),
    ("DISPLAY_CATEGORIES_ON_MENU", "categories", "category"),
)


@pytest.mark.parametrize(("setting", "collection", "current"), NAV_CASES)
def test_nav_marks_only_the_current_entry(render, setting, collection, current):
    """Each menu section highlights the entry the page being rendered belongs to.

    The two sections compute their own flag, and the category one used to test the flag
    belonging to the pages loop. Jinja scopes a ``{% set %}`` to the loop that made it,
    so the name was undefined there and no category was ever marked.

    ``aria-current`` is what carries this to a screen reader; the class only drives the
    styling.
    """
    here = SimpleNamespace(name="Notes", title="Notes", url="notes.html")
    elsewhere = SimpleNamespace(name="Other", title="Other", url="other.html")
    # Categories arrive as (term, articles) pairs, pages as a flat list.
    items = [here, elsewhere]
    if collection == "categories":
        items = [(item, []) for item in items]
    doc = render(**{setting: True, collection: items, current: here})

    entries = list(doc(".navbar-nav li").items())
    assert [classes(entry) for entry in entries] == ["nav-item active", "nav-item"]
    assert [entry.find("a").attr("aria-current") for entry in entries] == ["page", None]


def test_search_box_hidden_by_default(render):
    assert not render()("#sitesearch-input")


def test_search_box_uses_bootstrap_icon(render):
    """The theme dropped Font Awesome in 4.0.0 and loads Bootstrap Icons only."""
    doc = render(STORK_SEARCH=True)
    assert doc("#sitesearch-input")
    assert classes(doc("label[for=sitesearch-input] i")) == "bi bi-search"


@pytest.mark.parametrize("template", ALL_TEMPLATES)
def test_no_font_awesome_icons(jinja_env, template):
    """No template may reference an icon set the theme does not load."""
    source = jinja_env.loader.get_source(jinja_env, template)[0]
    assert "fa-" not in source


def test_footer_reports_versions(render):
    details = render()("footer details")
    assert "Pelican v4.12.0" in details.text()
    assert "Plumage v5.0.0.dev0" in details.text()


@pytest.mark.parametrize("deprecated", ["text-muted", "text-dark"])
def test_no_deprecated_color_utilities(render, deprecated):
    """Bootstrap 5.3 replaced these with utilities that follow the color scheme."""
    assert not render()(f".{deprecated}")


def test_feeds_are_advertised(render):
    doc = render(FEED_ALL_ATOM="feeds/all.atom.xml", FEED_DOMAIN="https://example.com")
    feed = doc("link[rel=alternate]")
    assert feed.attr("href") == "https://example.com/feeds/all.atom.xml"
    assert feed.attr("type") == "application/atom+xml"


TRANSLATED_CONTENT = {
    "title": "Bonjour",
    "url": "bonjour.html",
    "lang": "fr",
    "content": "<p>Salut.</p>",
    "date": datetime(2026, 1, 2, tzinfo=UTC),
    "locale_date": "2 January 2026",
}
"""One translated article or page, as a dict.

Jinja falls back to item lookup when the attribute is missing, so every field a given
template does not read is undefined rather than an ``AttributeError``.
"""

ENTRY_TEMPLATES = (("article.html", "article"), ("page.html", "page"))
"""The two templates rendering a single entry, and the name each binds it to."""


def translation(lang: str, url: str) -> SimpleNamespace:
    """Stand-in for the sibling entries Pelican hangs off ``translations``."""
    return SimpleNamespace(lang=lang, url=url)


def test_html_lang_defaults_to_the_site_language(render):
    """Nothing on a site-level listing carries a language of its own."""
    assert render().attr("lang") == "en"


@pytest.mark.parametrize(
    ("template", "name"),
    [("article.html", "article"), ("page.html", "page"), ("projects.html", "page")],
)
def test_html_lang_follows_the_content(render, template, name):
    """A translation declares its own language instead of the site-wide default."""
    doc = render(template, PROJECTS=[], tags=[], **{name: TRANSLATED_CONTENT})
    assert doc.attr("lang") == "fr"


@pytest.mark.parametrize(("template", "name"), ENTRY_TEMPLATES)
def test_translations_are_advertised_in_the_head(render, template, name):
    """The visible links say nothing to a crawler. These say it is the same document."""
    entry = TRANSLATED_CONTENT | {
        "translations": [
            translation("en", "hello.html"),
            translation("de", "hallo.html"),
        ]
    }
    links = render(template, **{name: entry})("head link[rel=alternate][hreflang]")
    assert {link.get("hreflang"): link.get("href") for link in links} == {
        "en": "/hello.html",
        "de": "/hallo.html",
    }


@pytest.mark.parametrize(("template", "name"), ENTRY_TEMPLATES)
def test_no_hreflang_without_a_translation(render, template, name):
    doc = render(template, **{name: TRANSLATED_CONTENT})
    assert not doc("head link[rel=alternate][hreflang]")


@pytest.mark.parametrize(("template", "name"), ENTRY_TEMPLATES)
def test_visible_translation_links_carry_their_language(render, template, name):
    entry = TRANSLATED_CONTENT | {"translations": [translation("en", "hello.html")]}
    link = render(template, **{name: entry})("main#content a[hreflang]")
    assert link.attr("hreflang") == "en"


def test_meta_description_falls_back_to_the_site_subtitle(render):
    doc = render(SITESUBTITLE="<em>Notes</em> on things")
    assert doc("meta[name=description]").attr("content") == "Notes on things"


def test_no_meta_description_without_a_subtitle(render):
    assert not render()("meta[name=description]")


@pytest.mark.parametrize(("template", "name"), ENTRY_TEMPLATES)
@pytest.mark.parametrize(
    ("fields", "expected"),
    [
        ({"summary": "<p>Derived from the body.</p>"}, "Derived from the body."),
        # An explicit Description: wins over the summary Pelican derives.
        (
            {"summary": "<p>Derived.</p>", "description": "Hand-written."},
            "Hand-written.",
        ),
    ],
    ids=["summary", "description"],
)
def test_meta_description_comes_from_the_entry(
    render, template, name, fields, expected
):
    """The site-wide subtitle is displaced rather than joined by a second tag."""
    doc = render(
        template, SITESUBTITLE="Site subtitle", **{name: TRANSLATED_CONTENT | fields}
    )
    assert doc("meta[name=description]").attr("content") == expected
    assert len(doc("meta[name=description]")) == 1


def test_article_shows_when_it_was_last_modified(render):
    stamp = datetime(2026, 3, 4, tzinfo=UTC)
    article = TRANSLATED_CONTENT | {
        "modified": stamp,
        "locale_modified": "4 March 2026",
    }
    sidebar = render("article.html", article=article)("#content ~ div time")
    assert sidebar.eq(1).attr("datetime") == stamp.isoformat()
    assert "4 March 2026" in sidebar.eq(1).text()


def test_article_without_a_modified_date_shows_none(render):
    doc = render("article.html", article=TRANSLATED_CONTENT)
    assert len(doc("#content ~ div time")) == 1


def test_analytics_markup_is_passed_through(render):
    """Pelican's own ANALYTICS setting takes whatever the provider hands you."""
    doc = render(ANALYTICS='<script src="https://example.com/count.js"></script>')
    assert doc("head script[src='https://example.com/count.js']")


def test_google_analytics_still_works(render):
    assert "G-ABC123" in render(GOOGLE_ANALYTICS="G-ABC123")("head").text()


@pytest.mark.parametrize(
    ("block", "displaced"),
    [
        # Block name, and a selector matching what that region renders by default.
        ("header", "h1 a.text-body-emphasis"),
        ("nav", "nav.navbar"),
        ("footer", "footer .row"),
    ],
)
def test_base_regions_are_overridable(render, render_override, block, displaced):
    """A theme extending Plumage swaps one region instead of copying base.html."""
    # Assert the selector matches something first, so the check below cannot pass by
    # naming a region that was never there.
    assert render()(displaced)
    doc = render_override(block, "<p id='replaced'>Mine</p>")
    assert doc("#replaced")
    # The region's own content is replaced, not pushed aside.
    assert not doc(displaced)


EMPTY_INDEX = {"articles_page": SimpleNamespace(object_list=[])}


def test_empty_site_lists_its_pages(render):
    pages = [SimpleNamespace(title="About", url="about.html")]
    doc = render("index.html", pages=pages, **EMPTY_INDEX)
    assert doc("main#content li a").attr("href") == "/about.html"


def test_site_with_nothing_at_all_says_so(render):
    doc = render("index.html", **EMPTY_INDEX)
    assert "no content yet" in doc("main#content").text()


TAXONOMY_FEEDS = (
    # Template name the term is bound to, the setting holding its feed pattern, and
    # the label the advertised feed carries.
    ("category", "CATEGORY_FEED_ATOM", "Category: Notes"),
    ("category", "CATEGORY_FEED_RSS", "Category: Notes"),
    ("tag", "TAG_FEED_ATOM", "Tag: Notes"),
    ("tag", "TAG_FEED_RSS", "Tag: Notes"),
)


@pytest.mark.parametrize(("name", "setting", "label"), TAXONOMY_FEEDS)
def test_taxonomy_feed_advertised(render, name, setting, label):
    term = SimpleNamespace(name="Notes", slug="notes")
    doc = render(
        FEED_DOMAIN="https://example.com", **{setting: "feeds/{slug}.xml", name: term}
    )
    feed = doc("link[rel=alternate]")
    assert feed.attr("href") == "https://example.com/feeds/notes.xml"
    assert label in feed.attr("title")


@pytest.mark.parametrize(
    ("name", "setting"), [(name, setting) for name, setting, _ in TAXONOMY_FEEDS]
)
def test_taxonomy_feed_skipped_for_a_term_bound_to_none(render, name, setting):
    """Pelican 4.12.0 made an article's category optional.

    It binds the name to None on the page of an article carrying none, where earlier
    releases left it out entirely. Both have to render, and neither may advertise a
    feed: the term the pattern interpolates does not exist. The undefined case is
    covered by every other render here, as the base context declares neither name.
    """
    doc = render(**{setting: "feeds/{slug}.xml", name: None})
    assert not doc("link[rel=alternate]")


@pytest.mark.parametrize(
    ("context", "expected"),
    [
        ({}, "index, follow"),
        ({"page": "a-draft", "drafts": ["a-draft"]}, "noindex, nofollow"),
        (
            {"page": "a-hidden-page", "hidden_pages": ["a-hidden-page"]},
            "noindex, nofollow",
        ),
    ],
)
def test_robots_meta(render, context, expected):
    assert render(**context)("meta[name=robots]").attr("content") == expected
