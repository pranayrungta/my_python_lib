from __main__ import *

import Pranay.files_structure.filenameGen as fileGen
try: valid_file_blocks
except NameError: valid_file_blocks=fileGen.parameter_generator(
    all_parameters,vary_parameter,for_all_fixed,
    constant_parameter, base, fileStructure, out_folder )

import numpy
# function searches for threshold fnode and return not_found if not found
def xCrit_value(filepath):
    data = numpy.loadtxt(filepath)
    x,y = using(data)
    for i in range(1,len(data)):
        if( (y[i-1]-threshold)*(y[i]-threshold) < 0 ):
            return x[i]
    return not_found

# fileData = [ (filepath1,vary1),
#              (filepath2,vary2),]
def x_at_yList(fileData):
    values = dict()
    for filepath,vary in fileData:
        xAty = xCrit_value(filepath)
        xval = float(vary.split('=')[-1])
        values[xval]= xAty
    return values

def header():
    global xlabel
    if(xlabel=='auto'):
        xlabel = all_parameters[vary_parameter][0]
        xlabel = xlabel.split('=')[0]
    head = "# %s\t%s\n"%(xlabel,ylabel)
    return head

for outfile, title, fileData in valid_file_blocks:
    outfile += '_th=%s'%threshold+'.txt'
    title += ' threshold=%s'%threshold
    f=open(outfile, 'w')
    f.write('# %s \n'%title )
    f.write('# not found : %s \n'%not_found)
    f.write('#\n' + header() )

    data = x_at_yList(fileData)
    for key,values in sorted(data.items()):
        f.write('%s\t%s\n'%(key, values) )
    f.close()
