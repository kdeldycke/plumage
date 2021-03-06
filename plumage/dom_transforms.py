# -*- coding: utf-8 -*-
#
# Copyright Kevin Deldycke <kevin@deldycke.com> and contributors.
# All Rights Reserved.
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

from urllib.parse import urlparse

from pyquery import PyQuery as pq


def transform(path, context):

    BASE_URL = urlparse(context.get("SITEURL", ""))

    # XXX This direct construct is stripping the "<!DOCTYPE>" heading. See:
    # https://github.com/gawel/pyquery/issues/199
    doc = pq(filename=path)

    # Add bootstrap table style to table elements.
    doc("#content table").add_class("table table-hover")
    doc("#content table thead th").attr("scope", "col")

    # Style TOC permalinks produced by Python's markdown.extensions.toc:
    # https://python-markdown.github.io/extensions/toc/
    doc(".headerlink").add_class("text-decoration-none small pl-2")

    # Make images responsive and styled in article content, but ignore
    # images in cards (like those from project template), images attached to
    # links, and emojis rendered as images.
    main_images_selector = (
        "#content img:not(.card-img-top):not(.link-icon):not(.emojione)"
    )
    doc(main_images_selector).add_class("img-fluid border rounded shadow")

    # Process all images from the main content to create a reduced set with
    # lower dimensions.
    # XXX Hack to bypass the bug on extenal images from image-process
    # plugin: https://github.com/pelican-plugins/image-process/issues/33

    def exclude_external_images(_, this):
        source = urlparse(this.get("src", ""))
        if (source.scheme and BASE_URL.scheme) and (source.netloc != BASE_URL.netloc):
            return False
        return True

    doc(main_images_selector).filter(exclude_external_images).add_class(
        "image-process-article-photo"
    )

    # Style blockquotes in the way Bootstrap does.
    doc("blockquote").add_class("blockquote border-left border-primary pl-3")

    # Style code boxes.
    doc(".codehilite, .highlight").add_class(
        f"pygments-style-{context.get('CODE_STYLE')} rounded shadow-sm mb-3"
    )

    # Style admonitions produced by Python Markdown into alerts.
    doc(".admonition").add_class("alert shadow").attr("role", "alert")
    doc(".admonition-title").add_class("alert-heading h4")
    # Map rST's admonition types to Bootstrap's:
    # https://python-markdown.github.io/extensions/admonition/#syntax
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

    # Tipue Search results styling.
    doc("#tipue_search_results_count").add_class("text-muted small float-right")
    doc("#tipue_search_image_modal").add_class("d-none")
    doc(".tipue_search_result").add_class("border-bottom border-secondary mb-4 pb-3")
    doc(".tipue_search_content_title").add_class("h3")
    doc(".tipue_search_content_bold").add_class("bg-warning rounded px-1")
    doc(".tipue_search_content_url").add_class("small text-info")
    doc(".tipue_search_image").add_class("float-left border rounded")
    doc(".tipue_search_note").add_class("d-none")

    # Save result.
    with open(path, "w") as source:
        source.write(doc.outerHtml())
