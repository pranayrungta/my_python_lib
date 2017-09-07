from __main__ import *

#---------generate filenames------------
if(fileStructure=='raw'):
    from Pranay.files_structure.filepath import raw_file_path as file_path
elif(fileStructure=='lib'):
    from Pranay.files_structure.filepath import lib_file_path as file_path
from Pranay.files_structure.filenameGen import *
#-----------------------------------------
valid_file_blocks = parameter_generator( all_parameters, vary_parameter,
           for_all_fixed, constant_parameter, base, file_path, out_folder )

if(output=='display_files'):
    print 'valid_file_blocks=\\'
    import pprint
    pp = pprint.PrettyPrinter(indent=4,width=200)
    pp.pprint(valid_file_blocks)
elif( len(valid_file_blocks)==0 ):
    print 'No files to be plotted'
else:
    import numpy as np
    import matplotlib.pyplot as plt
    #import matplotlib as mpl; mpl.style.use('classic')

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
