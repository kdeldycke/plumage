# -*- coding: utf-8 -*-
#
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
from .favicon import add_favicon_assets
from .webassets import setup_webassets


ALL_CODE_STYLES = {
    f.stem for f in PLUMAGE_ROOT.joinpath("static/css/pygments/").resolve().iterdir()
}


def register_signals():
    signals.initialized.connect(check_config)
    signals.static_generator_finalized.connect(add_favicon_assets)
    signals.content_written.connect(transform)


def check_config(sender):
    """ Validates and setup Plumage configuration. """
    conf = sender.settings

    # Keep some metadata around.
    conf["PELICAN_VERSION"] = pelican.__version__

    # Check code coloe scheme ID.
    conf = check_codestyle(conf)

    # Setup webassets plugin.
    conf = setup_webassets(conf)

    sender.settings = conf


def check_codestyle(conf):
    """Check selected code color scheme ID is recognized by Pygments.

    Defaults to "monokai" if none set in Pelican's conf.
    """
    # Defaults code style to Monokai.
    if not conf.get("CODE_STYLE"):
        conf["CODE_STYLE"] = "monokai"

    code_style = conf["CODE_STYLE"]
    if code_style not in ALL_CODE_STYLES:
        raise ValueError(
            f"{code_style} not recognized among {sorted(ALL_CODE_STYLES)}."
        )

    return conf
