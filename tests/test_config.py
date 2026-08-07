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

"""Checks on settings validation and on the metadata the theme hands to Pelican."""

from __future__ import annotations

from types import SimpleNamespace

import pytest

import plumage
from plumage import PLUMAGE_ROOT, config


def test_get_path_points_at_the_theme():
    theme = plumage.get_path()
    assert (PLUMAGE_ROOT / "templates" / "base.html").is_file()
    assert theme == str(PLUMAGE_ROOT)


def test_code_styles_match_shipped_stylesheets():
    """Every selectable style needs the stylesheet base.html asks webassets for."""
    assert config.ALL_CODE_STYLES
    for style in config.ALL_CODE_STYLES:
        assert (PLUMAGE_ROOT / "static" / "css" / "pygments" / f"{style}.css").is_file()


@pytest.mark.parametrize("style", ["monokai", "dracula", "github-dark", "nord"])
def test_known_code_style_is_kept(style):
    assert config.check_codestyle({"CODE_STYLE": style})["CODE_STYLE"] == style


@pytest.mark.parametrize("conf", [{}, {"CODE_STYLE": None}, {"CODE_STYLE": ""}])
def test_code_style_defaults_to_monokai(conf):
    assert config.check_codestyle(conf)["CODE_STYLE"] == "monokai"


@pytest.mark.parametrize("style", ["stata", "not-a-pygments-style"])
def test_unknown_code_style_is_rejected(style):
    with pytest.raises(ValueError, match=style):
        config.check_codestyle({"CODE_STYLE": style})


def test_check_config_exposes_versions(monkeypatch):
    """Templates render both versions in the footer, so both must reach settings."""
    # Sidestep the npm toolchain the webassets pipeline would otherwise install.
    monkeypatch.setattr(config, "setup_webassets", lambda conf: conf)
    sender = SimpleNamespace(settings={})

    config.check_config(sender)

    assert sender.settings["PLUMAGE_VERSION"] == plumage.__version__
    assert sender.settings["PELICAN_VERSION"]
    assert sender.settings["CODE_STYLE"] == "monokai"
