<img src="docs/figs/pylettes_logo.png" width=400, padding=100>


## Pylettes
### v0.1.0

[![GitHub tag (latest by date)](https://img.shields.io/github/v/tag/fcomitani/pylettes)](https://github.com/fcomitani/pylettes/releases/tag/v0.1.0)
[![PyPI](https://img.shields.io/pypi/v/pylettes)](https://pypi.org/project/pylettes/)
[![Licence](https://img.shields.io/github/license/fcomitani/pylettes)](https://github.com/fcomitani/pylettes/blob/main/LICENSE)
[![GitHub top language](https://img.shields.io/github/languages/top/fcomitani/pylettes)](https://github.com/fcomitani/pylettes/search?l=python)
<!-- [![Documentation Status](https://readthedocs.org/projects/pylettes-cluster/badge/?version=latest)](https://pylettes-cluster.#readthedocs.io/en/latest/?badge=latest) -->


`pylettes` is a lightweight `matplotlib`-compatible collection of beautiful palettes for Python 3.

### Installation

`pylettes` can be easily installed with `PiPy`

`pip install pylettes`.

To install the latest (unreleased) version you can download it from this repository by running 
 
    git clone https://github.com/fcomitani/pylettes
    cd pylettes
    python setup.py install

The only requirement is `matplotlib >= 1.3.1`.

### Usage

Palettes can be imported directly from the `pylettes` package.
They can be transformed into `matplotlib` color maps by instantiating the class and calling its `cmap` attribute.

    from pylettes import Acapulco2Paris

    custom_cmap = Acapulco2Paris().cmap

The `show_colors` method allows you to visualize and inspect any palette.

    Acapulco2Paris().show_colors()
<img src="docs/figs/acapulco_colors.png" width=400, padding=100>

The list of colors can be visualized as a continuous scale by providing the `continuous` argument.

    Acapulco2Paris().show_colors(continuous=True)
<img src="docs/figs/acapulco_colors_continuous.png" width=400, padding=100>

Palettes can be reversed with activating the `reverse` flag upon initialization.

    Acapulco2Paris(reverse=True).show_colors()
<img src="docs/figs/acapulco_colors_reverse.png" width=400, padding=100>

Finally, all currently available palettes can be inspected with `list_all_palettes()`. 
While `search_palettes_by_tag()` allows you to search palettes by keywords.
For example, you can obtain all colorblind-friendly palettes with

    from pylettes import search_palettes_by_tag

    for palette in list_palettes_by_tag('colorblind'):
        palette().show_colors()


<!-- ### Citation

When using this library, please cite

-->

### Contributions

I plan to keep this library updated and add more choices with time. 
New palette submissions are welcome!
