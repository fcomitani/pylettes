from pylettes.base import Palette


class Triangle(Palette):
    """ Triangle - 220830 """

    colors = ('#40BBBB', '#A34AC6', '#FFAC58')
    tags = ['categorical']


class Tol(Palette):
    """ Tol - 220902 
    Paul Tol 2021
    https://personal.sron.nl/~pault/
    """

    colors = ('#332288', '#117733', '#44AA99', '#88CCEE',
              '#DDCC77', '#CC6677', '#AA4499', '#882255')
    tags = ['categorical', 'Tol', 'colorblind']


class OkabeIto(Palette):
    """ OkabeIto - 220902 
    Okabe & Ito 2002
    https://jfly.uni-koeln.de/color/#pallet
    """

    colors = ('#000000', '#E69F00', '#56B4E9', '#009E73',
              '#F0E442', '#0072B2', '#D55E00', '#CC79A7')
    tags = ['categorical', 'Okabe & Ito', 'Okabe', 'Ito', 'colorblind']


if __name__ == "__main__":
    pass
