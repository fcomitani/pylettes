from typing import List, Collection
import sys
import inspect

import matplotlib.pyplot as plt

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


def list_all_tags() -> List:
    """ Returns all available tags.

    :return: list, the list of all available tags.
    """

    return list(set([tag for tags in
                    [palette.tags for palette in list_all_palettes()]
                    for tag in tags]))


def show_multiple_palettes(palettes: Collection[Palette],
                           save_name: str = None) -> None:
    """ Displays the colors that make up multiple palettes.

    :param palettes: Collection, list of palettes to plot.
    :param save_name: str, if not None, path and file name of where the palette
        plot will be saved.
    """

    all_colors = [palette.colors for palette in palettes]
    max_length = max([len(colors) for colors in all_colors])

    fig = plt.figure(figsize=(max_length*.9, len(palettes)*1.1))
    gs = fig.add_gridspec(len(palettes), 1)
    
    for i, palette in enumerate(palettes):

        palette=palette()
    
        ax = []

        ax.append(fig.add_subplot(gs[i, 0]))
        plt.sca(ax[-1])

        ax[-1].set_facecolor('white')
        plt.axis('off')

        plt.scatter(range(len(palette)), [0]*len(palette), c=palette.colors,
                    marker='s', s=2500)

        plt.title(str(palette), fontsize=20, loc='left', color='#333333')
        plt.xlim([-.5, max_length-.5])

    plt.tight_layout()

    if save_name is not None:
        save_name += '.png' if not save_name.endswith('.png') else ''
        plt.savefig(save_name, dpi=300, bbox_inches='tight')
