# eg. 'Smallworld_dynamic_n=100_k=2_b=0_p=0.1.txt'
# eg1. 'ring_n=100_k=1_b=0.1.txt'
# eg2. 'ScaleFree_order=4_b=0.1.txt'

fetch_parameters = [
    ('Smallworld','dynamic', 'n=100','k=2', 'b=$', 'p=0.1') ,
    ('Smallworld','static', 'n=100','k=2', 'b=$', 'p=$') ,
    ('ring','n=100','k=1','b=$'),
    ('ScaleFree','order=4','b=$')       ]







#--------------------------------------
import sys
sys.dont_write_bytecode = True
from Pranay.files_structure.fetch_data import *
