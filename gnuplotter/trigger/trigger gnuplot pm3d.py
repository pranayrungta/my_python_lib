criteria = ['spacetime','.txt']
nonCriteria=['$', ]

base = './sample_data'
fileStructure = 'raw' # 'raw' 'lib'

out_folder = 'None' # 'None' 'fol_name' 'auto'
#----------------------------------------
terminal = 'jpeg' # 'jpeg' 'png' 'eps' 'display_files'

xlabel = 'time'
ylabel = 'x'

using_colms = (1,2,3)
plot = False # True False





import sys
sys.dont_write_bytecode = True
from Pranay.gnuplotter.gnuplotpm3d import *
