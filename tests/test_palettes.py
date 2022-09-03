import os
import shutil

import pytest
from pylettes import *
from pylettes.base import Palette


class TestPalettes:

    @pytest.mark.parametrize("palette", list_all_palettes())
    def test_attributes(self, palette: Palette) -> None:

        palette.name
        palette.colors
        palette.tags

        palette().show_colors()
        palette().show_colors(continuous=True)
        palette(reverse=True).show_colors()


if __name__ == '__main__':
    pass
