# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 22:32:45 2019

@author: Jesus
"""

import matplotlib as mpl
from matplotlib.lines import Line2D

def tableau_colors():
    """
    Args:

    Returns:
        dictionary of {color (str) : RGB (tuple) for the dark tableau20 colors}
    """
    tableau20 = [(31, 119, 180), (174, 199, 232), (255, 127, 14), (255, 187, 120),
                 (44, 160, 44), (152, 223, 138), (214, 39, 40), (255, 152, 150),
                 (148, 103, 189), (197, 176, 213), (140, 86, 75), (196, 156, 148),
                 (227, 119, 194), (247, 182, 210), (127, 127, 127), (199, 199, 199),
                 (188, 189, 34), (219, 219, 141), (23, 190, 207), (158, 218, 229)]

    for i in range(len(tableau20)):
        r, g, b = tableau20[i]
        tableau20[i] = (r / 255., g / 255., b / 255.)
    names = ['blue', 'orange', 'green', 'red', 'purple', 'brown', 'pink', 'gray', 'yellow', 'turquoise']
    colors = [tableau20[i] for i in range(0, 20, 2)]

    return dict(zip(names,colors))

def set_rc_params():
    """
    Args:

    Returns:
        dictionary of settings for mpl.rcParams
    """
    params = {'axes.linewidth' : 1.5,
              'axes.unicode_minus' : False,
              'figure.dpi' : 300,
              'font.size' : 20,
              'legend.frameon' : True,
              'legend.handletextpad' : 0.4,
              'legend.handlelength' : 1,
              'legend.facecolor' : 'white',
              'legend.fancybox'  : True,
              'legend.fontsize' : 12,
              'mathtext.default' : 'regular',
              'savefig.bbox' : 'tight',
              'xtick.labelsize' : 12,
              'ytick.labelsize' : 12,
              'xtick.major.size' : 6,
              'ytick.major.size' : 6,
              'xtick.major.width' : 1,
              'ytick.major.width' : 1,
              'xtick.top' : True,
              'ytick.right' : True,
              'axes.edgecolor' : 'black',
              'savefig.facecolor'   : 'white',
              'axes.facecolor'   : 'whitesmoke',
              'font.family' : 'sans',
              'font.monospace' : 'computer modern roman',
              'text.usetex' : True,
              'axes.grid' : True,
              'grid.color' :   'gray',
              'grid.linestyle' :   '-',
              'grid.linewidth'  :   0.2,
              'grid.alpha'       :   0.3,
              'axes.axisbelow'      : 'line'
              }
    for p in params:
        mpl.rcParams[p] = params[p]
    return params

def main():
    set_rc_params()
    tab = tableau_colors()

if __name__ == "__main__":
    main()
    