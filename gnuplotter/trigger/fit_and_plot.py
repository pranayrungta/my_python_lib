all_parameters = [['Smallworld'],#0
                  ['static',],#1
                  ['n=100','n=200','n=400', ] , #2
                  ['k=2'] , #3
                  ['b=0'] , #4
                  ['th=0.01'], #5
                  ]
vary_parameter = 2  # index
for_all_fixed = 1   # index
constant_parameter = { 0:0 ,
                       3:0 ,
                       4:0 ,
                       5:0 ,
                       }

base = './../../matplotlib/trigger/sample_data'
fileStructure = 'raw' # 'lib' 'raw'

out_folder='None' # 'auto' 'None' 'FOLDER'
#-----gnuplot parameters-------------
fit = 'power' # 'power' 'linear'

terminal = 'jpeg'  # 'eps' 'jpeg' 'png' 'display_files'

xlabel = 'p'
xRangeflag = False  # True   False
xRange = (0,5)

ylabel = 'Critical coupling'
yRangeflag = False # True   False
yRange = (-0.05,1.05)

plot_With = 'p'   # 'lp'  'p' 'l'  'errorbars'
using_colms = (1,2)

plot = False  # True   False
set_grid = False  # True   False
#------------------------------------




import sys
sys.dont_write_bytecode = True
from Pranay.gnuplotter.fit_plot import *
