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

base = './../../matplotlib/trigger/sample_data'
fileStructure = 'lib' # 'lib' 'raw'

out_folder = 'None' # 'None' 'fol_name' 'auto'
#-----gnuplot parameters-------------
terminal = 'png'  #'show' 'eps' 'jpeg' 'png'
set_grid = True  # True   False

xlabel = 'N1/N scaled'
xRangeflag = False  # True   False
xRange = (0,5)

ylabel = '<x>'
yRangeflag = False # True   False
yRange = (-0.05,1.05)

plot_With = 'p'   # 'lp'  'p' 'l'  'errorbars'
#using_colms = (1,2)
def colmGen():
    nRange=[100,250,500]
    x,y=1,2
    xcrit=0.125; power=0.5
    for n in nRange:
        colms = '( ($%s/%s-%s)*(%s**%s) ):%s'%(
                    x,n,xcrit,n,power,y)
        yield colms

plot = False  # True   False
#------------------------------------





import sys
sys.dont_write_bytecode = True
from Pranay.gnuplotter.finiteSize import *
