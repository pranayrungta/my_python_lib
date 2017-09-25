from __main__ import *
import Pranay.files_structure.filenameGen as fileGen

try: valid_file_blocks
except NameError: valid_file_blocks=fileGen.parameter_generator(
    all_parameters,vary_parameter,for_all_fixed,
    constant_parameter, base, fileStructure, out_folder )

if( len(valid_file_blocks)==0 ):
    print('No files to be plotted')
elif(output=='display_files'):
    fileGen.display(valid_file_blocks)
else:
    import numpy as np
    import matplotlib.pyplot as plt
    import matplotlib as mpl; mpl.style.use('classic')

    for outfile,title,fileData in valid_file_blocks:
        plt.grid(set_grid)

        if('x' in log):plt.xscale('log')
        if('y' in log):plt.yscale('log')
        plt.xlabel(*xlabel); plt.ylabel(*ylabel)
        plt.xlim(**xlim); plt.ylim(**ylim)

        for filepath,curve_title in fileData:
            data = np.loadtxt(filepath)
            plt.plot( *using(data), label=curve_title )

        if(plot_title=='auto'): plt.title(title)
        elif(plot_title!='None'):plt.title(plot_title)
        if(legend_loc!='None'):plt.legend( loc=legend_loc )
        plt.tight_layout()
        if(output=='show'): plt.show()
        else: plt.savefig( '%s.%s'%(outfile,output) )    
        plt.close()
