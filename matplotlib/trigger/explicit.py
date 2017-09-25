valid_file_blocks=[
    [   'dynamic_c=1_k=2_b=-0.1_p=0.9',
        'dynamic c=1 k=2 b=-0.1 p=0.9',
        [   ('./sample_data//dynamic/c=1/k=2/n=100/b=-0.1/dynamic_c=1_k=2_n=100_b=-0.1_p=0.9.txt', 'n=100'),
            ('./sample_data//dynamic/c=1/k=2/n=250/b=-0.1/dynamic_c=1_k=2_n=250_b=-0.1_p=0.9.txt', 'n=250'),
            ('./sample_data//dynamic/c=1/k=2/n=500/b=-0.1/dynamic_c=1_k=2_n=500_b=-0.1_p=0.9.txt', 'n=500')]],
    [   'dynamic_c=1_k=4_b=-0.1_p=0.9',
        'dynamic c=1 k=4 b=-0.1 p=0.9',
        [   ('./sample_data//dynamic/c=1/k=4/n=100/b=-0.1/dynamic_c=1_k=4_n=100_b=-0.1_p=0.9.txt', 'n=100'),
            ('./sample_data//dynamic/c=1/k=4/n=250/b=-0.1/dynamic_c=1_k=4_n=250_b=-0.1_p=0.9.txt', 'n=250'),
            ('./sample_data//dynamic/c=1/k=4/n=500/b=-0.1/dynamic_c=1_k=4_n=500_b=-0.1_p=0.9.txt', 'n=500')]]]

#---------plot parameters-------------
log = 'None' #'None' 'x' 'y' 'xy'

xlabel = ( r'$N_1$', {'fontsize':35} )
ylabel = ( '<x>', {'fontsize':20} ) #{'fontsize':20}

xlim={} #{'xmin':-0.1, 'xmax':1}
ylim={} #{'ymin':-0.1, 'ymax':1}

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
