all_parameters = [['freq'],#0
                  ['btc'],#1
                  [ 'Ring','RSF_k=1_ic=100','RSF_k=2_ic=100','Star' ] , #2
                  ]

vary_parameter = 2  # index
for_all_fixed = 1   # index
constant_parameter = { 0:0 ,
                       }

base = './../../gnuplotter/trigger/sample_data/'
fileStructure = 'raw' # 'lib' 'raw'
    
out_folder = 'None' # 'None' 'fol_name' 'auto'
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

plot = True  # True   False
set_grid = True  # True   False
#------------------------------------





import sys
sys.dont_write_bytecode = True
from Pranay.gnuplotter.gnuplotter import *
