from __main__ import *

import os
files = [filename for filename in os.listdir('./')
         if( all(x in filename for x in criteria) )]


if( len(files)==0 ):
    print('No files to be plotted')
else:
    import Pranay.gnuplotter.gnuplotter_basic as plt
    plt.initialize(terminal, False, None, using_colms)
    plt.script.write("set pm3d map \n")
    plt.setAxis(xlabel,ylabel, None,None,False,False)
    for filename in files:
        title = ' '.join( filename[0:-4].split("_") )
        plt.output(filename[0:-4],title)
        plt.script.write("splot '%s' using %s\n\n\n"%(filename, plt.colm) )
    plt.draw(plot)
