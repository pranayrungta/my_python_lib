criteria = ['.spt','']

output = 'show' # 'show' 'png' 'pdf' 'eps'


xlim={} #{'xmin':1, 'xmax':50}
ylim={} #{'ymin':1, 'ymax':50}

xlabel = 'auto' # 'auto'
ylabel = 'auto'  # 'auto'
title = 'auto' # None  'auto'  'TITLE'

colorRange = 'auto' # 'auto'  [0,1]

figsize = (10,6)
vertical_on_x = True # False  True





import sys
sys.dont_write_bytecode = True
from Pranay.matplotlib.matplotlibpm3d import *
