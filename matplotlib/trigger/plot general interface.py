all_parameters = [['freq'],#0
                  ['btc'],#1
                  ['Ring','RSF_k=1_ic=100', 'RSF_k=2_ic=100', 'Star', 'Star1'],#2
                  ]


vary_parameter = 2  # index
for_all_fixed = 1   # index
constant_parameter = { 0:0 ,
                       }

base = './../../gnuplotter/trigger/sample_data/'
fileStructure = 'raw' # 'lib' 'raw'

out_folder = 'None' # 'None' 'fol_name' 'auto'
#---------plot parameters-------------
output = 'show'  # 'eps' 'pdf' 'png' 'show'
log = 'None' #'None' 'x' 'y' 'xy'

xlabel = 'fnode'
ylabel = 'Mean BS'
label_para = {} # {'fontsize':20}

xRange = 'auto' # 'auto' (0.1,1)
yRange = 'auto' # 'auto' (-0.05,1.05)

plot_style = 'o-'   # 'ro-'
using_colms = (0,2)

set_grid = True  # True   False
legend_loc = 'best' # 'best', 'right', 'upper right',
action = 'plot' # 'display_files' 'plot'
#------------------------------------





import sys
sys.dont_write_bytecode = True
from Pranay.matplotlib.lib_plotter import *
