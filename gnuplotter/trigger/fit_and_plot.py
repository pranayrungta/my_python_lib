all_parameters = [['static', 'dynamic'],#0
                  ['c=1'] , #1
                  ['k=2', 'k=4'] , #2
                  ['n=100','n=250','n=500', ] , #3
                  ['b=0'] , #4
                  ['p=0.1','p=0.3','p=0.5','p=0.7',], #5
                  ]
vary_parameter = 3  # index
for_all_fixed = 0   # index
constant_parameter = { 1:0 ,
                       2:0 ,
                       4:0 ,
                       5:0 ,
                       }

base = './../../matplotlib/trigger/sample_data'
fileStructure = 'lib' # 'lib' 'raw'

out_folder='None' # 'auto' 'None' 'FOLDER'
#-----gnuplot parameters-------------
fit = 'power' # 'power' 'linear'

terminal = 'display_files'  # 'eps' 'jpeg' 'png' 'display_files'

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
