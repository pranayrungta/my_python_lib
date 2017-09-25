from __main__ import *

#-----maintaining backward compatibility----
try: out_folder 
except NameError: out_folder='auto'
#--------------------------------------------

import Pranay.files_structure.filenameGen as fileGen
try: valid_file_blocks
except NameError: valid_file_blocks=fileGen.parameter_generator(
    all_parameters,vary_parameter,for_all_fixed,
    constant_parameter, base, fileStructure, out_folder )


if( len(valid_file_blocks)==0 ):
    print('No files to be plotted')
elif(terminal=='display_files'):
    fileGen.display(valid_file_blocks)
else:
    import Pranay.gnuplotter.gnuplotter_basic as plt
    plt.initialize(terminal,set_grid, plot_With, using_colms)
    plt.setAxis(xlabel,ylabel,xRange,yRange,xRangeflag,yRangeflag)
    for outfile, title, fileData in valid_file_blocks:
        plt.output(outfile,title)
        plt.plot(fileData)
    plt.draw(plot)
#-----------------------------------------
