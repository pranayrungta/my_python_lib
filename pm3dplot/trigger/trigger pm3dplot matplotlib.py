criteria = ['.spt','']

output = 'png' # 'show' 'png' 'pdf' 'eps'

xlabel = 'auto' # 'auto'
xRange = 'auto'# [1,50] # 'auto'

ylabel = 'auto'  # 'auto'
yRange =  [1,50] # 'auto'

title = 'auto' # None  'auto'  'title'
# 'auto' set filename as title

colorRange = [-1,1.5]  #   'auto'

vertical_on_x = True # False  True





import sys
sys.dont_write_bytecode = True
from Pranay.pm3dplot.matplotlibpm3d import *
