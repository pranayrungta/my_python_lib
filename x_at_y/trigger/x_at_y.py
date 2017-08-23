all_parameters = [['ring'],#0
                  ['n=8','n=12','n=16','n=20','n=24',],#1
                  [ 'k=2' ] , #2
                  [ 'b=0' ] , #3
                  ]
vary_parameter = 1  # index
for_all_fixed = 2   # index
constant_parameter = {0:0,
                      3:0,
                      }
base = './../../Data/'

fileStructure = 'lib' # 'lib' 'raw'
   


threshold = 0.5
using_colms = (0,1) # 0 is first colm

x_at_y_label = 'critical coupling'
not_found = -1  # 'N.A.'  'not_found'  -1
#----------------------------------------------------------------








import sys
sys.dont_write_bytecode = True
from Pranay.x_at_y.x_at_y_module import *
