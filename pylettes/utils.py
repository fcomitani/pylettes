from typing import List
import sys
import inspect

from pylettes.sequential import *
from pylettes.categorical import *


_all_palettes = [palette[1] for palette in inspect.getmembers(sys.modules[__name__], inspect.isclass)
                if palette[0] != 'Palette']


def list_palettes_by_tag(tag: str) -> List:
    """ Search palettes by a given tag.

    :param tag: str, the tag used to select palettes.
    :return: list, the list of palettes to which the tag
        was assigned.
    """

    return [palette for palette in _all_palettes if tag in palette.tags]
    
    
def list_all_palettes() -> List:
    """ Returns all available palettes.

    :return: list, the list of all available palettes.
    """

    return _all_palettes
    
