all_parameters = [['freq'],#0
                  ['btc'],#1
                  ['Ring', 'RSF_k=1_ic=100', 'RSF_k=2_ic=100', 'Star', 'Star1'],#2
                  ]


vary_parameter = 2  # index
for_all_fixed = 1   # index
constant_parameter = { 0:0 ,
                       }

base = './../../gnuplotter/trigger/sample_data/'
fileStructure = 'raw' # 'lib' 'raw'

out_folder = 'None' # 'None' 'fol_name' 'auto'
#---------plot parameters-------------
log = 'None' #'None' 'x' 'y' 'xy'

xlabel = 'fnode'
ylabel = 'Mean BS'
label_para = {} # {'fontsize':20}

xlim={} #{'xmin':-0.1, 'xmax':1}
ylim={'ymin':-100, 'ymax':7000} #{'ymin':-0.1, 'ymax':1}

def using(colm):
    return colm[:,0], colm[:,1], 'o' # 'ro-'

set_grid = False  # True   False
plot_title = 'auto' # 'auto' 'None' 'TITLE'
legend_loc = 'best' # 'None' 'best', 'right'
output = 'show'  # 'display_files' 'show' 'eps' 'png'
#------------------------------------





import sys
sys.dont_write_bytecode = True
from Pranay.matplotlib.lib_plotter import *
