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

import logging
import os
from pathlib import Path
from shutil import which
from textwrap import indent

import pelican
from pelican import signals
from pelican.contents import Static
from pynpm import NPMPackage

from . import logger, PLUMAGE_ROOT
from .dom_transforms import transform


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

        # Register the new asset along other static files.
        sender.context["staticfiles"].append(static)
