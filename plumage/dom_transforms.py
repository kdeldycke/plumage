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

from pyquery import PyQuery as pq


def transform(path, context):
    """Rewrite a page in place, adding the Bootstrap classes the theme's styles hang off.

    Connected to Pelican's ``content_written`` signal, which hands over the path of the
    page just written and the site context. Nothing below reads the context: every
    rewrite is driven by the markup alone.
    """
    # XXX This direct construct is stripping the "<!DOCTYPE>" heading. See:
    # https://github.com/gawel/pyquery/issues/199
    #
    # Both ends of the round-trip name their encoding. Pelican writes UTF-8, but neither
    # pyquery's open() nor the one below passes an encoding of its own, so both would
    # otherwise take the platform default: cp1252 on Windows, which raises on the first
    # accented character anywhere in a site.
    doc = pq(filename=path, encoding="utf-8")

    # Add bootstrap table style to table elements.
    doc("#content table").add_class("table table-hover")
    doc("#content table thead th").attr("scope", "col")

    # Make images responsive and styled in article content, but ignore
    # images in cards (like those from project template), and images attached to
    # links.
    main_images_selector = "#content img:not(.card-img-top):not(.link-icon)"
    doc(main_images_selector).add_class("img-fluid border rounded shadow")

    # Style blockquotes in the way Bootstrap does.
    doc("blockquote").add_class(
        "blockquote border-start border-primary-subtle bg-dark-subtle fs-6 border-4 ps-2",
    )
    doc("blockquote p").add_class("p-2")

    # Give every code block the .highlight container the styling hangs off.
    #
    # Which markup a block arrives in depends on the reader and renderer that produced the
    # page, and only one of the three needs help. reStructuredText's `code-block` and
    # MyST's Sphinx renderer both wrap the block in a <div class="highlight">, but MyST's
    # docutils renderer, the one it uses for any document without an intra-site link, a
    # bibliography or maths, emits a bare <pre class="code ... literal-block">.
    #
    # That distinction is invisible until it is not: every stylesheet under
    # static/css/pygments/ is generated with `-a ".highlight"`, and code.scss is scoped the
    # same way, so a block that never gets the class renders with no syntax colors at all.
    # Pygments still emits the token spans, and nothing selects them.
    #
    # Matching on `code` as well as `literal-block` keeps plain docutils literal blocks,
    # which carry no lexer output, out of it. The wrap has to happen before the styling
    # below, so the containers it creates are styled too.
    doc("pre.code.literal-block").wrap('<div class="highlight"></div>')

    # Style code boxes.
    doc(".highlight").add_class("rounded shadow-sm mb-3")

    # Style admonitions into alerts. Both of the renderers MyST picks between emit the
    # same `.admonition` hook, differing only in the element carrying it: <aside> from
    # the docutils one, <div> from Sphinx. reStructuredText's directives land there too.
    doc(".admonition").add_class("alert shadow").attr("role", "alert")
    doc(".admonition-title").add_class("alert-heading h4")
    # Map the admonition types those readers emit onto Bootstrap's alert variants. The
    # docutils set is the wider one, and the MyST directive names line up with it:
    # https://docutils.sourceforge.io/docs/ref/rst/directives.html#admonitions
    admo_map = {
        "primary": {"primary"},
        "secondary": {"secondary"},
        "success": {"success"},
        "danger": {"danger", "error"},
        "warning": {"warning", "attention", "caution", "important"},
        "info": {"info", "hint", "note", "tip"},
        "light": {"light"},
        "dark": {"dark"},
    }
    for bootstrap_class, admo_classes in admo_map.items():
        for admo_class in admo_classes:
            doc(f".admonition.{admo_class}").add_class(f"alert-{bootstrap_class}")

    # Save result.
    with open(path, "w", encoding="utf-8") as source:
        source.write(doc.outerHtml())
