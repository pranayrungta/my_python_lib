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

base = './sample_data/'
fileStructure = 'lib' # 'lib' 'raw'

out_folder = 'None' # 'None' 'fol_name' 'auto'
#---------plot parameters-------------
log = 'None' #'None' 'x' 'y' 'xy'

xlabel = ( 'N1/N scaled', {'fontsize':35} )
ylabel = ( '<x>', {'fontsize':20} ) #{'fontsize':20}

xlim={'xmin':-3, 'xmax':3} #{'xmin':-0.1, 'xmax':1}
ylim={} #{'ymin':-0.1, 'ymax':1}

def using_colms():
    nRange = [100.0,250.0,500.0]
    xcrit = 0.125
    power = 0.5
    x1,y1 = 0,1
    for n in nRange:
        colm = yield # getting data from file
        x,y = colm[:,x1],colm[:,y1]
        yield (x/n-xcrit)*(n**power), y, 'o' # 'ro-'

set_grid = False  # True   False
plot_title = 'auto' # 'auto' 'None' 'TITLE'
legend_loc = 'best' # 'None' 'best', 'right'
output = 'show'  # 'display_files' 'show' 'eps' 'png'
#------------------------------------





import sys
sys.dont_write_bytecode = True
from Pranay.matplotlib.finiteSize import *
