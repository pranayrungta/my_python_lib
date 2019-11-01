all_parameters = [['dynamic', 'static'],#0
                  ['c=1'],#1
                  [ 'k=2','k=4' ] , #2
                  [ 'n=100','n=250','n=500' ] , #3
                  [ 'b=-0.1' ] , #4
                  [ 'p=0.9' ] , #5
                  ]

vary_parameter = 3  # index
for_all_fixed = 2   # index
constant_parameter = { 0:0 ,
                       1:0 ,
                       4:0 ,
                       5:0 ,
                       }

base = './../sample_data/'
fileStructure = 'lib' # 'lib' 'raw'

out_folder = 'None' # 'None' 'fol_name' 'auto'

#---------plot parameters-------------
log = 'None' #'None' 'x' 'y' 'xy'

xlabel = ( r'$N_1$', dict(fontsize=25) )
ylabel = ( '<x>',  dict(fontsize=25) ) #{'fontsize':20}

xlim= dict()#dict(xmin=-0.1, xmax=1)
ylim= dict()#dict(ymin=-0.1, ymax=1)

def using(colm):
    return colm[:,0], colm[:,1], 'o-' # 'ro-'

set_grid = False  # True   False
plot_title = 'auto' # 'auto' 'None' 'TITLE'
legend_loc = 'best' # 'None' 'best', 'right'
output = 'show'  # 'display_files' 'show' 'eps' 'png'
#------------------------------------





import sys
sys.dont_write_bytecode = True
from Pranay.matplotlib.lib_plotter import *
