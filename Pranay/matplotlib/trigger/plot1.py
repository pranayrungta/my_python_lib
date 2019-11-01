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
#---------plot parameters-------------
log = 'None' #'None' 'x' 'y' 'xy'

xlabel = ( r'fnode', {'fontsize':20} )
ylabel = ( 'Mean BS', {'fontsize':20} ) #{'fontsize':20}

xlim={'xmin':0.1, 'xmax':1}#{'xmin':-0.1, 'xmax':1}
ylim={'ymin':-0.1, 'ymax':100} #{'ymin':-0.1, 'ymax':1}

def using(colm):
    if(colm.ndim==1): #contains single line
        colm=colm.reshape(1,len(colm))
    return colm[:,0], colm[:,1], 'x-' # 'ro-'

set_grid = True  # True   False
plot_title = 'auto' # 'auto' 'None' 'TITLE'
legend_loc = 'best' # 'None' 'best', 'right'
output = 'show'  # 'display_files' 'show' 'eps' 'png'
#------------------------------------




import sys
sys.dont_write_bytecode = True
from Pranay.matplotlib.lib_plotter import *
