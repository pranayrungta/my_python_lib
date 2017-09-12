from __main__ import *

#-----maintaining backward compatibility----
try: out_folder 
except NameError: out_folder='auto'
#--------------------------------------------
from Pranay.files_structure.filenameGen import *
from Pranay.gnuplotter.gnuplotter_basic import *

def plotBlock(fileData):
    return plotStatement(fileData,filenameClause)


#------------main program-------------------
valid_file_blocks = parameter_generator(all_parameters,vary_parameter,
      for_all_fixed,constant_parameter,base,fileStructure,out_folder)
if(len(valid_file_blocks)>0):
    generate_script(valid_file_blocks, '.', plotBlock)
    if(plot):
        os.system('gnuplot script.plt')
        os.remove('script.plt')
else:
    print '\nNo files found'
#-----------------------------------------
