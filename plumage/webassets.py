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
from pathlib import Path
from shutil import which
from textwrap import indent
from typing import Any
import importlib

from pynpm import NPMPackage

from . import PLUMAGE_ROOT, logger

"""Setup the `webassets <https://github.com/miracle2k/webassets>`_ plugin for Pelican.
"""


CONFIG_DEFAULTS: dict[str, str] = {
    # No need to force a compressed rendering, a minification pass is applied
    # at the end of the pipeline. See:
    # https://webassets.readthedocs.io/en/latest/builtin_filters.html#webassets.filter.libsass.LibSass
    # "LIBSASS_STYLE": "compressed",
}
"""Default configuration for `webassets <https://github.com/miracle2k/webassets>`_.

See the `list of configuration parameters for each filter
<https://webassets.readthedocs.io/en/latest/builtin_filters.html>`_.
"""


POSTCSS_CLI_NAME = "postcss"
"""Name of the PostCSS CLI binary."""

CLOSURE_JAR_NAME = "closure.jar"
"""Name of the Closure CLI jar file."""


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

        # Install Node dependencies.
        logger.info(
            f"Install Plumage's Node.js dependencies from {node_deps_file}:\n"
            f"{indent(node_deps_file.read_text(), ' ' * 2)}",
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
        "POSTCSS": postcss_bin,
        # Force usage of autoprefixer via PostCSS.
        "POSTCSS_EXTRA_ARGS": ["--use", "autoprefixer"],
    }


def closure_config():
    """Locate the Closure CLI jar file provided by the ``closure`` package.

    .. warning::

        We need to locate the ``closure`` Python package without loading it, as it is
        old and unmaintained and produce the following error on calling
        ``import closure``:

            .. code-block:: pytb
                Traceback (most recent call last):
                File "<string>", line 1, in <module>
                File ".../python3.12/site-packages/closure/__init__.py", line 3, in <module>
                    from pkg_resources import resource_filename
                ModuleNotFoundError: No module named 'pkg_resources'
    """
    package = importlib.util.find_spec("closure")
    closure_jar = (Path(package.origin).parent / CLOSURE_JAR_NAME).resolve()
    logger.info(f"{CLOSURE_JAR_NAME} JAR file found at {closure_jar}")
    return {
        "CLOSURE_COMPRESSOR_PATH": str(closure_jar),
    }


def setup_webassets(conf: dict[str, Any]) -> dict[str, Any]:
    """Setup pelican-webassets plugin configuration."""
    # Merge static and dynamic configurations to produce webassets' defaults.
    default_conf = CONFIG_DEFAULTS.copy() | postcss_config() | closure_config()

    # Update the default configuration with user-defined values.
    webassets_conf = default_conf | dict(conf.get("WEBASSETS_CONFIG", {}))

    # Save updated configuration in Pelican settings in the form of ``(key, value)``
    # instead of a ``dict`` as expected by ``webassets`` plugin. See:
    # https://github.com/pelican-plugins/webassets/blob/2.0.0/README.md#webassets_config
    conf["WEBASSETS_CONFIG"] = list(webassets_conf.items())

    return conf
