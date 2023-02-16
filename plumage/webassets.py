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

import os
from shutil import which
from textwrap import indent

from pynpm import NPMPackage

from . import logger, PLUMAGE_ROOT


def setup_webassets(conf):
    """Setup pelican-webassets plugin configuration."""
    if not conf.get("WEBASSETS_CONFIG"):
        conf["WEBASSETS_CONFIG"] = []
    webassets_conf_keys = {i[0] for i in conf.get("WEBASSETS_CONFIG")}

    # Search for PostCSS binary location.
    cli_name = "postcss"

    # The dependency definition file relative to Plumage's install path takes
    # precedence.
    node_deps_file = PLUMAGE_ROOT.joinpath("package.json").resolve()
    node_bin_path = node_deps_file.parent / "node_modules" / ".bin"
    cli_search_path = [
        str(node_bin_path),
    ]

    # Check if the path exist in any of the environment locations.
    env_path = ":".join(cli_search_path + [os.getenv("PATH")])
    postcss_bin = which(cli_name, path=env_path)

    if not postcss_bin:
        logger.warning(f"{cli_name} CLI not found.")

        # Install Node dependencies.
        logger.info(
            f"Install Plumage's Node.js dependencies from {node_deps_file}:\n"
            f"{indent(node_deps_file.read_text(), ' ' * 2)}"
        )
        pkg = NPMPackage(node_deps_file)
        try:
            pkg.install()
        except FileNotFoundError:
            logger.error("npm CLI not found.")
            raise

        postcss_bin = which(cli_name, path=env_path)
        assert postcss_bin

    # Register PostCSS to webassets plugin.
    logger.info(f"{cli_name} CLI found at {postcss_bin}")
    if "POSTCSS_BIN" not in webassets_conf_keys:
        conf["WEBASSETS_CONFIG"].append(
            ("POSTCSS_BIN", postcss_bin),
        )

    # Force usage of autoprefixer via PostCSS.
    if "POSTCSS_EXTRA_ARGS" not in webassets_conf_keys:
        conf["WEBASSETS_CONFIG"].append(
            ("POSTCSS_EXTRA_ARGS", ["--use", "autoprefixer"]),
        )

    return conf
