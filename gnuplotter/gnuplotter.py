from __main__ import *

#-----maintaining backward compatibility----
try: out_folder 
except NameError: out_folder='auto'


#---------generate filenames------------
if(fileStructure=='raw'):
    from Pranay.files_structure.filepath import raw_file_path as file_path
elif(fileStructure=='lib'):
    from Pranay.files_structure.filepath import lib_file_path as file_path
from Pranay.files_structure.filenameGen import *
def generate_parameters():
    return parameter_generator(all_parameters,vary_parameter,
      for_all_fixed,constant_parameter,base,file_path,out_folder)
#-----------------------------------------


from Pranay.gnuplotter.gnuplotter_basic import *
def plotBlock(fileData):
    return plotStatement(fileData,filenameClause)


#------------main program-------------------
valid_file_blocks = generate_parameters()
if(len(valid_file_blocks)>0):
    generate_script(valid_file_blocks, '.', plotBlock)
    if(plot):
        os.system('gnuplot script.plt')
        os.remove('script.plt')
else:
    print '\nNo files found'
#-----------------------------------------
