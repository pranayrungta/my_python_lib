filename = 'sample_data/critical_fnode.txt'
outfilename = 'fc_SW_static_n=100_c=1'
fontSize = 13

xlabel = ( 'Characteristic Path Length', {'fontsize':18} )
ylabel = ( r'$f_c$', {'fontsize':22} ) #{'fontsize':20}

xlim={} #{'xmin':5, 'xmax':9.5}
ylim={} #{'ymin':0.1, 'ymax':0.42}

log = 'None' #'None' 'x' 'y' 'xy'

plot_with = dict(marker='o',  #'+'  '.'  'o'  '*'  'p'  's'  'x'  'D'  'h'  '^' 
            markerSize=8, linestyle =  ':' # '-'  '--'  ':'  '-.' 'None'
)
output_format = 'show' # 'show' 'png' 'pdf' 'eps'

# [ index, (x,y), 'label' ]
plot_details = [ [0,(3,2),'RSF m=1'],
                 [1,(3,2),'RSF m=2'],
                 [2,(3,2),'DSF'],
                 [3,(3,2),'SW'],
                 ]
legend = True
iteractive = True # True:only runs in ipython cmd False

text_labels = [     #SW
                    [8.91, 0.157, 'p=0.2'] ,
                    [7.582, 0.177, 'p=0.3'] ,
                    [6.754, 0.217, 'p=0.4'] ,
                    [6.375, 0.285, 'p=0.5'] ,
                    [6.056, 0.325, 'p=0.6'] ,
                    [5.813, 0.365, 'p=0.7'] ,
                    [5.68, 0.395, 'p=0.8'] ,
                    [4.72, 0.375, 'p=0.9'] ,

                    #RSF k=1
                    [ 4.15 , 0.028, 'N=100' ],
                    [ 5.20 , 0.028, 'N=200' ],
                    [ 6.02 , 0.015, 'N=400' ],

                    #RSF k=2
                    [ 2.56 , 0.375, 'N=100' ],
                    [ 2.72 , 0.425, 'N=200' ],
                    [ 3.70 , 0.40, 'N=400' ],

                    #DSF
                    [ 2.85 , 0.26, 'N=27' ],
                    [ 3.68 , 0.2, 'N=81' ],
                    [ 4.55 , 0.16, 'N=243' ],
                ]
    

##----------------------------------------------------
import sys
sys.dont_write_bytecode = True
from Pranay.matplotlib.plot_index import *
