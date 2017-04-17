from __main__ import *

#---------check using_colms for backward compatibility---
try:
  using_colms
except NameError:
  using_colms=(0,1)
#--------------------------------------------------------


#---------generate filenames------------
if(fileStructure=='raw'):
    from Pranay.files_structure.filepath import raw_file_path as file_path
elif(fileStructure=='lib'):
    from Pranay.files_structure.filepath import lib_file_path as file_path
from Pranay.files_structure.filenameGen import *
def generate_parameters():
    return parameter_generator(all_parameters,vary_parameter,
            for_all_fixed,constant_parameter,base,file_path)
#-----------------------------------------





from Pranay.x_at_y.x_at_y_base import *
#---------main program---------------------------
def header():
    xaxislabel = all_parameters[vary_parameter][0]
    xaxislabel = xaxislabel.split('=')[0]
    head = "# %s\t%s\n"%(xaxislabel,x_at_y_label)
    return head

fileData = generate_parameters()
for outfile, title, files in fileData:
    outfile += '_th=%s'%threshold+'.txt'
    title += ' threshold=%s'%threshold
    f=open(outfile, 'w')
    f.write('# %s \n'%title )
    f.write('# code %s : not found\n'%not_found)
    f.write('#\n' + header() )

    data = x_at_yList(files,threshold,not_found,using_colms)
    for key,values in sorted(data.items()):
        f.write('%s\t%s\n'%(key, values) )
    f.close()
