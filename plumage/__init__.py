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
from pathlib import Path

__version__ = "3.1.1"

""" Examples of valid version strings according :pep:`440#version-scheme`:

.. code-block:: python
    __version__ = "1.2.3.dev1"  # Development release 1
    __version__ = "1.2.3a1"  # Alpha Release 1
    __version__ = "1.2.3b1"  # Beta Release 1
    __version__ = "1.2.3rc1"  # RC Release 1
    __version__ = "1.2.3"  # Final Release
    __version__ = "1.2.3.post1"  # Post Release 1
"""


logger = logging.getLogger(__name__)

PLUMAGE_ROOT = Path(__file__).resolve().parent


def get_path() -> str:
    """Returns installation path of the theme.

    Used in ``pelicanconf.py`` to dynamiccaly fetch theme location on the system.
    """
    return str(PLUMAGE_ROOT)


# Workaround circular dependencies.
from .config import register_signals  # noqa: E402

register_signals()
