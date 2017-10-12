from __main__ import *

import Pranay.files_structure.criteria as fileGen
try: valid_file_blocks
except NameError: valid_file_blocks = fileGen.parameter_generator(
    criteria, nonCriteria, base, fileStructure, out_folder)

if( len(valid_file_blocks)==0 ):
    print('No files to be plotted')
elif(terminal=='display_files'):
    fileGen.display(valid_file_blocks)
else:
    import Pranay.gnuplotter.gnuplotter_basic as plt
    plt.initialize(terminal, False, None, using_colms)
    plt.script.write("set pm3d map \n")
    plt.setAxis(xlabel,ylabel, None,None,False,False)
    for outfile,title,infile in valid_file_blocks:        
        plt.output(outfile,title)
        plt.script.write("splot '%s' using %s\n\n\n"%(infile, plt.colm) )
    plt.draw(plot)
