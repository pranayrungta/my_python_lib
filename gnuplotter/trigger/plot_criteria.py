##    ('together','auto') produces outfile as
##    criteria joined from [1:]

all_parameters =[
    [
        ('together','auto'), # ('individual',),  ('together','outfile'), 
        ['.txt', 'freq'],# criteria
        ['$', '$',],# non-criteria
    ],
    [
        ('individual',), # ('individual',),  ('together','outfile'), 
        ['.txt', 'freq'],# criteria
        ['$', '$',],# non-criteria
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
from Pranay.gnuplotter.gnuplot_criteria_based import *
