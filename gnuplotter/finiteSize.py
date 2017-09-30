from __main__ import *

import Pranay.files_structure.filenameGen as fileGen
try: valid_file_blocks
except NameError: valid_file_blocks=fileGen.parameter_generator(
    all_parameters,vary_parameter,for_all_fixed,
    constant_parameter, base, fileStructure, out_folder )

import Pranay.gnuplotter.gnuplotter_basic as plt
def filenameClause(filepath,curve_title,colm):
    return  '"%s" u %s w %s title "%s"'%(
        filepath, colm, plot_With, curve_title)

def plotfiles(fileData):
    clauses = [ filenameClause(filepath,curve_title,colm)
                    for (filepath,curve_title),colm
                            in zip( fileData,colmGen() ) ]
    clauses[0] = 'plot '+ clauses[0]
    clauseSep = ', \t \\\n     '
    plt.script.write( clauseSep.join(clauses)+'\n\n' )


if( len(valid_file_blocks)==0 ):
    print('No files to be plotted')
elif(terminal=='display_files'):
    fileGen.display(valid_file_blocks)
else:
    plt.initialize(terminal,set_grid, plot_With)
    plt.setAxis(xlabel,ylabel,xRange,yRange,xRangeflag,yRangeflag)
    for outfile, title, fileData in valid_file_blocks:
        plt.output(outfile,title)
        plotfiles(fileData)
    plt.draw(plot)
