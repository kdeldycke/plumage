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

"""Setup the `webassets <https://github.com/miracle2k/webassets>`_ plugin for Pelican."""

import os
from shutil import which
from textwrap import indent
from typing import Any

from pynpm import NPMPackage

from . import PLUMAGE_ROOT, logger

POSTCSS_CLI_NAME = "postcss"
"""Name of the PostCSS CLI binary."""


def postcss_config():
    """Produce the default configuration for PostCSS.

    Takes care of:

        - Installing PostCSS CLI and its dependency with ``npm``.
        - Locating the PostCSS CLI binary on the filesystem.
        - Registering PostCSS to the webassets plugin.
    """
    # The dependency definition file relative to Plumage's install path takes
    # precedence.
    node_deps_file = PLUMAGE_ROOT.joinpath("package.json").resolve()
    node_bin_path = node_deps_file.parent / "node_modules" / ".bin"
    cli_search_path = [
        str(node_bin_path),
    ]

    # Check if the path exist in any of the environment locations.
    env_path = os.pathsep.join([*cli_search_path, os.getenv("PATH")])
    postcss_bin = which(POSTCSS_CLI_NAME, path=env_path)

    if not postcss_bin:
        logger.warning(f"{POSTCSS_CLI_NAME} CLI not found.")

        # Install Node dependencies. The manifest is read as UTF-8, which JSON is by
        # spec, rather than as whatever the platform defaults to: cp1252 on Windows.
        logger.info(
            f"Install Plumage's Node.js dependencies from {node_deps_file}:\n"
            f"{indent(node_deps_file.read_text(encoding='utf-8'), ' ' * 2)}",
        )
        pkg = NPMPackage(node_deps_file)
        try:
            pkg.install()
        except FileNotFoundError:
            logger.error("npm CLI not found.")
            raise

        postcss_bin = which(POSTCSS_CLI_NAME, path=env_path)
        assert postcss_bin

    logger.info(f"{POSTCSS_CLI_NAME} CLI found at {postcss_bin}")

    return {
        "POSTCSS_BIN": postcss_bin,
        # Force usage of autoprefixer via PostCSS.
        "POSTCSS_EXTRA_ARGS": ["--use", "autoprefixer"],
    }


def setup_webassets(conf: dict[str, Any]) -> dict[str, Any]:
    """Setup pelican-webassets plugin configuration."""
    # PostCSS is the only filter the theme configures. In particular no LIBSASS_STYLE:
    # the {% assets %} pipeline in base.html ends on a cssmin pass, so asking libsass for
    # compressed output too would only do the same work twice. See the parameters each
    # filter accepts: https://webassets.readthedocs.io/en/latest/builtin_filters.html
    #
    # Update the defaults with user-defined values.
    webassets_conf = postcss_config() | dict(conf.get("WEBASSETS_CONFIG", {}))

    # Save updated configuration in Pelican settings in the form of ``(key, value)``
    # instead of a ``dict`` as expected by ``webassets`` plugin. See:
    # https://github.com/pelican-plugins/webassets/blob/2.0.0/README.md#webassets_config
    conf["WEBASSETS_CONFIG"] = list(webassets_conf.items())

    return conf
