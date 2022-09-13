import os
import shutil

import pytest
from pylettes import *
from pylettes.base import Palette


class TestPalettes:

    def test_utils(self) -> None:

        list_all_palettes()
        list_palettes_by_tag('sequential')
        list_palettes_by_tag('categorical')
        list_palettes_by_tag('colorblind')
        
    @pytest.mark.parametrize("palette", list_all_palettes())
    def test_attributes(self, palette: Palette) -> None:

        palette.name
        palette.colors
        palette.tags
        
        len(palette())
        str(palette())
        palette()[0]	

        palette().show_colors()
        palette().show_colors(continuous=True)
        palette(reverse=True).show_colors()


if __name__ == '__main__':
    pass
