from __main__ import *

import numpy
import Pranay.files_structure.filenameGen as fileGen
#---------check using_colms for backward compatibility---
try: using_colms
except NameError:using_colms=(0,1)
#--------------------------------------------------------

# function searches for threshold fnode and return not_found if not found
def xCrit_value(filepath,threshold,not_found,colms):
    col0,col1 = colms
    data = numpy.loadtxt(filepath)
    for i in range(1,len(data)):
        if( (data[i-1][col1]-threshold)*
            (data[i][col1]  -threshold) < 0 ):
            return data[i][col0]
    return not_found

# fileData = [ (filepath1,vary1),
#              (filepath2,vary2),]
def x_at_yList(fileData,threshold,not_found,colms):
    values = {}
    for filepath,vary in fileData:
        xAty = xCrit_value(filepath,threshold,not_found,colms)
        xval = float(vary.split('=')[-1])
        values[xval]= xAty
    return values

def header():
    xaxislabel = all_parameters[vary_parameter][0]
    xaxislabel = xaxislabel.split('=')[0]
    head = "# %s\t%s\n"%(xaxislabel,x_at_y_label)
    return head

valid_file_blocks=fileGen.parameter_generator(all_parameters,vary_parameter,
                          for_all_fixed,constant_parameter,base,fileStructure)
for outfile, title, fileData in valid_file_blocks:
    outfile += '_th=%s'%threshold+'.txt'
    title += ' threshold=%s'%threshold
    f=open(outfile, 'w')
    f.write('# %s \n'%title )
    f.write('# code %s : not found\n'%not_found)
    f.write('#\n' + header() )

    data = x_at_yList(fileData,threshold,not_found,using_colms)
    for key,values in sorted(data.items()):
        f.write('%s\t%s\n'%(key, values) )
    f.close()
