all_parameters =[
    [
        {'outfile':'auto', 'title':'auto'},
        [
            ('freq_btc_Ring.txt', 'auto'),
            ('freq_btc_RSF_k=1_ic=100.txt', 'auto'),
            ('freq_btc_RSF_k=2_ic=100.txt', 'auto'),
            ('freq_btc_Star.txt', 'auto'),
        ]
    ],
    [
        {'outfile':'RSF_Star', 'title':'auto'},
        [
            ('freq_btc_RSF_k=1_ic=100.txt', 'auto'),
            ('freq_btc_RSF_k=2_ic=100.txt', 'k=2'),
            ('freq_btc_Star.txt', 'Star'),
        ]
    ],
]



base = './sample_data/'
fileStructure = 'raw' # 'lib' 'raw'
    
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

plot = True  # True   False
set_grid = True  # True   False
#------------------------------------


import sys
sys.dont_write_bytecode = True
from Pranay.gnuplotter.gnuplot_enumerated import *
