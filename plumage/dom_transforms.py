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

    # Make images responsive and styled in article content, but ignore
    # images in cards (like those from project template), and images attached to
    # links.
    main_images_selector = (
        "#content img:not(.card-img-top):not(.link-icon)"
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
    doc("blockquote").add_class(
        "blockquote border-start border-primary-subtle bg-dark-subtle fs-6 border-4 ps-2"
    )
    doc("blockquote p").add_class("p-2")

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

    # Save result.
    with open(path, "w") as source:
        source.write(doc.outerHtml())
