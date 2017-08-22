from __main__ import *

#---------generate filenames------------
if(fileStructure=='raw'):
    from Pranay.files_structure.filepath import raw_file_path as file_path
elif(fileStructure=='lib'):
    from Pranay.files_structure.filepath import lib_file_path as file_path
from Pranay.files_structure.filenameGen import *
#-----------------------------------------
valid_file_blocks = parameter_generator(all_parameters,vary_parameter,
                        for_all_fixed,constant_parameter,base,file_path)

if(output=='display_files'):
    print '---FILES TO BE PLOTTED----'
    print
    for out,tit,fileData in valid_file_blocks:
        print out
        for filepath,curve in fileData:
            print curve,filepath
        print
elif( len(valid_file_blocks)==0 ):
    print 'No files to be plotted'
else:
    #---------generate output folder-----------
    if(out_folder=='None'): folderName = './'
    elif(out_folder=='auto'):
        folderName = all_parameters[vary_parameter][0]
        folderName = 'varying ' + folderName.split('=')[0]
    else: folderName = out_folder
    if(not os.path.isdir(folderName) ): os.mkdir(folderName)
    #-----------------------------------------

    import numpy as np
    import matplotlib.pyplot as plt
    #x,y = using_colms

    for outfile,title,fileData in valid_file_blocks:
        plt.grid(set_grid)

        if('x' in log):plt.xscale('log')
        if('y' in log):plt.yscale('log')
        plt.xlabel(xlabel,**label_para)
        plt.ylabel(ylabel,**label_para)
        plt.xlim(**xlim)
        plt.ylim(**ylim)

        colms = using_colms()
        for filepath,curve_title in fileData:
            data = np.loadtxt(filepath)
            if(data.ndim==1): #contains single line
                data=data.reshape(1,len(data))
            colms.next()
            plt.plot( *colms.send(data), label=curve_title )

        if(plot_title=='auto'): plt.title(title)
        elif(plot_title!='None'):plt.title(plot_title)
        if(legend_loc!='None'):plt.legend( loc=legend_loc )
        plt.tight_layout()
        if(output=='show'): plt.show()
        else:
            plt.savefig( '%s/%s.%s'%(folderName,outfile,output) )    
        plt.close()
