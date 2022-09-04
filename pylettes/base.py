from abc import abstractmethod
from typing import Tuple, List, Union, Collection

import matplotlib.pyplot as plt
from matplotlib.colors import to_hex, to_rgb
from matplotlib.colors import LinearSegmentedColormap


class Palette:

    @property
    def name(self) -> str:
        """ Palette name. """

        return self.__class__.__name__

    @property
    @abstractmethod
    def colors(self) -> Tuple:
        """ Hex color tuple. """

        raise NotImplementedError

    @property
    @abstractmethod
    def tags(self) -> List:
        """ List of tags for easy search and access. """

        raise NotImplementedError

    def __init__(self, reverse: bool = False) -> None:
        """ Initialize the palette class
        by building it as cmap. 

        :param reverse: bool, if True reverse the colors order.
        """

        if reverse:
            self.colors = self.colors[::-1]
        self.cmap = LinearSegmentedColormap.from_list(self.name,
                                                      self.colors)
                                                      
    def __len__(self) -> None:
        """ The palette length. """
        return len(self.colors)
 
    def __repr__(self):
        """ String representation. """

        return self.name

    @classmethod
    def to_rgb(cls, colors: Union[Collection[str], str], unit: bool = False) \
            -> Union[Tuple[Tuple[float]], Tuple[float]]:
        """ Takes a color or a list of colors in hex format
        and converts them to RGB.

        :param colors: Collection or str, the color or list of colors to convert.
        :param unit: bool, if true return RGB values normalized to 1.
        :return: Tuple or Tuple of Tuple, the color converted as an (R, G, B) tuple.
        """

        if isinstance(colors, Collection):
            return [cls.to_rgb(color) for color in colors]
        return (int(colors[i:i+2], 16)/(255. if unit else 1.) for i in (0, 2, 4))

    def get_rgb(self) -> Tuple[Tuple]:
        """ Converts the full list of colors to the RGB format. 

        :return: Tuple of Tuple, the list of palette colors converted as RGB tuples.
        """

        return self.to_rgb(self.colors)

    def show_colors(self, continuous: bool = False,
                    save_name: Union[str, None] = None) -> None:
        """ Displays the colors that make up the palette.

        :param continuous: bool, if True, show the colors as a gradient.
        :param save_name: str, if not None, path and file name of where the palette
            plot will be saved.
        """

        fig = plt.figure(figsize=(len(self), 1))
        gs = fig.add_gridspec(1, 1)
        ax = []

        ax.append(fig.add_subplot(gs[0, 0]))
        plt.sca(ax[-1])

        ax[0].set_facecolor('white')
        plt.axis('off')

        if continuous:
            plt.scatter([x*len(self)/100. for x in range(100)], [0]*100, c=range(100), cmap=self.cmap,
                        marker='s', s=2500)
        else:
            plt.scatter(range(len(self)), [0]*len(self), c=self.colors,
                        marker='s', s=2500)

        plt.title(str(self), fontsize=20, loc='left', color='#333333')
        plt.xlim([-.5, len(self)-.5])

        if save_name is not None:
            save_name += '.png' if not save_name.endswith('.png') else ''
            plt.savefig(save_name, dpi=300, bbox_inches='tight')


if __name__ == "__main__":
    pass
