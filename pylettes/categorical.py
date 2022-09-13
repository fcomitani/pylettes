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


class Distinct16(Palette):
    """ Distinct16 - 220912 
    List of 20 highly distinct colors.
    """

    colors = ('#e6194B', '#3cb44b', '#ffe119', '#4363d8',
              '#f58231', '#42d4f4', '#f032e6', '#fabed4',
              '#469990', '#dcbeff', '#9A6324', '#fffac8',
              '#800000', '#aaffc3', '#000075', '#a9a9a9')
    tags = ['categorical', 'Distinct']


class Distinct20(Palette):
    """ Distinct16 - 220912 
    List of 20 highly distinct colors.
    """

    colors = ('#e6194B', '#3cb44b', '#ffe119', '#4363d8', '#f58231',
              '#911eb4', '#42d4f4', '#f032e6', '#bfef45', '#fabed4',
              '#469990', '#dcbeff', '#9A6324', '#fffac8', '#800000',
              '#aaffc3', '#808000', '#ffd8b1', '#000075', '#a9a9a9')
    tags = ['categorical', 'Distinct']


if __name__ == "__main__":
    pass
