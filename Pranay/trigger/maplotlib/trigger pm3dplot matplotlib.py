criteria = ['.spt','']

title = 'auto' # 'None'  'auto'  'TITLE'
xlabel = ( 'time',   {'fontsize':20} ) #( 'time',   {'fontsize':20} )
ylabel = ( r'$x_i$', {'fontsize':25} ) #( r'$x_i$', {'fontsize':25} ) 

xlim=dict() # dict(xmin=1, xmax=50)
ylim=dict() # dict(ymin=1, ymax=50)
colorRange = dict() # dict(vmin=0, vmax=1)

vertical_on_x = True # False  True
figsize = (8,4.5)
output = 'show' # 'show' 'png' 'pdf' 'eps'










import sys
sys.dont_write_bytecode = True
from Pranay.matplotlib.matplotlibpm3d import *
