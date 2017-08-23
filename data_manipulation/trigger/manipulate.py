all_parameters = [['Star'],#0
                  ['n=100',],#1
                  ['h','l'],#2
                  ['pc=1','pc=2','pc=4','pc=8','pc=16','pc=32','pc=50',
                   'pc=64','pc=70','pc=80','pc=90','pc=95','pc=99',] , #3
                  ]


vary_parameter = 3  # index
for_all_fixed = 2   # index
constant_parameter = { 0:0 ,
                       1:0 ,
                       }

base = './../CvsBS/Data/'
fileStructure = 'lib' # 'lib' 'raw'
    
#-----gnuplot parameters-------------
xlabel = 'c' # 'auto'
ylabel = 'BS' # 'auto'

using_colms = (0,1) # 1st col is 0
xval = [0.1, 1, 1.7]
#------------------------------------


import sys
sys.dont_write_bytecode = True
from Pranay.data_manipulation.restructure import *
