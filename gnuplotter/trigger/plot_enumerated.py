valid_file_blocks=\
[   [   'plot_0',
        'plot 0',
        [   ('./sample_data//freq_btc_Ring.txt', 'freq btc Ring'),
            ('./sample_data//freq_btc_RSF_k=1_ic=100.txt', 'freq btc RSF k=1 ic=100'),
            ('./sample_data//freq_btc_RSF_k=2_ic=100.txt', 'freq btc RSF k=2 ic=100'),
            ('./sample_data//freq_btc_Star.txt', 'freq btc Star')]],
    [   'RSF_Star',
        'RSF Star',
        [   ('./sample_data//freq_btc_RSF_k=1_ic=100.txt', 'freq btc RSF k=1 ic=100'),
            ('./sample_data//freq_btc_RSF_k=2_ic=100.txt', 'k=2'),
            ('./sample_data//freq_btc_Star.txt', 'Star')]]]

#-----gnuplot parameters-------------
terminal = 'jpeg'  # 'eps' 'jpeg' 'png'

xlabel = 'btc'
xRangeflag = False  # True   False
xRange = (0,5)

ylabel = 'prob'
yRangeflag = False # True   False
yRange = (-0.05,1.05)

plot_With = 'lp'   # 'lp'  'p' 'l'  'errorbars'
using_colms = (1,3)

plot = False  # True   False
set_grid = True  # True   False
#------------------------------------


import sys
sys.dont_write_bytecode = True
from Pranay.gnuplotter.gnuplot_enumerated import *
