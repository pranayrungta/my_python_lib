all_parameters = [['DSF'],#0
                  ['order=3','order=4','order=5'],#1
                  [ 'c=0.1','c=0.5','c=1','c=2','c=3','c=4', ] , #2
                  ]


vary_parameter = 2  # index
for_all_fixed = 1   # index
constant_parameter = { 0:0 ,
                       }

base = './'
fileStructure = 'raw' # 'lib' 'raw'
    
#-----gnuplot parameters-------------
terminal = 'jpeg'  # 'eps' 'jpeg' 'png'

xlabel = 'fnode'
xRangeflag = False  # True   False
xRange = (0,5)

ylabel = 'Mean BS'
yRangeflag = True # True   False
yRange = (-0.05,1.05)

plot_With = 'l'   # 'lp'  'p' 'l'  'errorbars'
using_colms = (1,2)

plot = False  # True   False
set_grid = True  # True   False
#------------------------------------





import sys
sys.dont_write_bytecode = True
from Pranay.gnuplotter.gnuplotter import *
