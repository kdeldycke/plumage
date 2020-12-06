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

from pathlib import Path

import pelican
from pelican import signals
from pelican.contents import Static

from .dom_transforms import transform


__version__ = "2.4.0"

""" Examples of valid version strings according :pep:`440#version-scheme`:

.. code-block:: python
    __version__ = '1.2.3.dev1'   # Development release 1
    __version__ = '1.2.3a1'      # Alpha Release 1
    __version__ = '1.2.3b1'      # Beta Release 1
    __version__ = '1.2.3rc1'     # RC Release 1
    __version__ = '1.2.3'        # Final Release
    __version__ = '1.2.3.post1'  # Post Release 1
"""


PLUMAGE_ROOT = Path(__file__).resolve().parent

ALL_CODE_STYLES = {
    f.stem for f in PLUMAGE_ROOT.joinpath("static/css/pygments/").resolve().iterdir()
}


def get_path():
    """Returns installation path of the theme.

    Used in ``pelicanconf.py`` to dynamiccaly fetch theme location on the
    system.
    """
    return str(PLUMAGE_ROOT)


def check_config(sender):
    """ Validates and setup Plumage configuration. """
    # Keep some metadata around.
    sender.settings["PELICAN_VERSION"] = pelican.__version__
    # Defaults code style to Monokai.
    if not sender.settings.get("CODE_STYLE"):
        sender.settings["CODE_STYLE"] = "monokai"
    code_style = sender.settings["CODE_STYLE"]
    if code_style not in ALL_CODE_STYLES:
        raise ValueError(
            f"{code_style} not recognized among {sorted(ALL_CODE_STYLES)}."
        )


def add_favicon_assets(sender):
    """Copy all individual files found in /static/favicon theme's folder
    to the root of the generated site.

    Favicons were generated with RealFaviconGenerator v0.16:
    https://realfavicongenerator.net
    """
    # Our theme structure expect default configuration.
    # See: https://docs.getpelican.com/en/latest/settings.html#themes
    assert "static" in sender.settings["THEME_STATIC_PATHS"]

    for asset in (PLUMAGE_ROOT / "static" / "favicon").iterdir():
        assert asset.is_file()

        # Add static file to generator context, as Pelican does natively at:
        # https://github.com/getpelican/pelican/blob/8033162ba4393db60791b201fb100d1be0f04431/pelican/generators.py#L811-L817
        static = sender.readers.read_file(
            base_path=asset.parent,
            path=asset.name,
            content_class=Static,
            fmt="static",
            context=sender.context,
            preread_signal=signals.static_generator_preread,
            preread_sender=sender,
            context_signal=signals.static_generator_context,
            context_sender=sender,
        )

        # Forces the asset to be saved at the root of the output folder.
        # See: https://github.com/getpelican/pelican/blob/8033162ba4393db60791b201fb100d1be0f04431/pelican/contents.py#L55-L59
        static.metadata["save_as"] = asset.name
        setattr(static, "override_save_as", asset.name)

        # Register asset along other static files.
        sender.context["staticfiles"].append(static)


signals.initialized.connect(check_config)
signals.static_generator_finalized.connect(add_favicon_assets)
signals.content_written.connect(transform)
