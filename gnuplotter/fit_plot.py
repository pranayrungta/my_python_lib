from __main__ import *

#---------generate filenames------------
from Pranay.files_structure.filenameGen import *
def generate_parameters():
    return parameter_generator(all_parameters,vary_parameter,
            for_all_fixed,constant_parameter,base,fileStructure)
#-----------------------------------------

from Pranay.gnuplotter.gnuplotter_basic import *
from Pranay.gnuplotter.fit_func import *

def plotClause(filepath,vary):
    return ( filenameClause(filepath,vary) + ', '+
             plot_fitCurve_clause(vary))

def plotBlock(fileData):
    s= fit_files(fileData,using_colms,fit) + '\n'
    s+= plotStatement(fileData,plotClause)
    return s


#------------main program-------------------
valid_file_blocks = generate_parameters()
if(len(valid_file_blocks)>0):
    folderName = all_parameters[vary_parameter][0]
    folderName = folderName.split('=')[0]
    folderName = 'varying '+folderName

    if(not os.path.isdir(folderName) ):
        os.mkdir(folderName)
    generate_script(valid_file_blocks,folderName,plotBlock)

    if(plot):
        os.system('gnuplot script.plt')
        os.remove('script.plt')
else:
    print '\nNo files found'
#-----------------------------------------
