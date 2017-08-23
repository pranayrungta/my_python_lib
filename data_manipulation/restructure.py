from __main__ import *

from Pranay.files_structure.filenameGen import *
#---------generate filenames------------
if(fileStructure=='raw'):
    from Pranay.files_structure.filepath import raw_file_path as file_path
elif(fileStructure=='lib'):
    from Pranay.files_structure.filepath import lib_file_path as file_path
#---------------------------------------

def file_value(paraDic,vary):
    value = eval(vary.split('=')[-1])
    filename = dicToParaValues(paraDic,all_parameters)
    filename = sortedList(filename)
    filename = '_'.join(filename)+'.txt'
    return filename,value

##return  [       (star,n=3),  #common name
##             [(filepath,val1),
##              (filepath,val2), ]
##        ]
def generateParameters():
    iterations = len(all_parameters[for_all_fixed])
    parameter = []
    for iter_no in range(iterations):
        paraDic = constant_parameter.copy()
        paraDic[for_all_fixed] = iter_no
        common_name = sortedList(dicToParaValues(paraDic,all_parameters))

        fileData=[]
        for v,vary in enumerate(all_parameters[vary_parameter]):
            paraDic[vary_parameter] = v
            filepath,val= file_value(paraDic,vary)
            filepath = file_path(filepath,base)
            fileData += [ (filepath, val) ]
        fileData = check_validity(fileData)
        if(len(fileData)>0):
            parameter += [ (common_name,fileData) ]
    return parameter

import numpy
def read_data(fileData):
    data = {}
    for filepath,vary in fileData:
        filedata = numpy.loadtxt(filepath)
        for line in filedata:
            x = line[using_colms[0]]
            y = line[using_colms[1]]
            if(not data.has_key(x)):
                data[x] = {}
            data[x][vary]=y
    return data
 
def writeFile(filename,header,dataDic):
    f=open(filename,'w')
    f.write(header)
    for key,val in sorted(data[x].iteritems()):
        f.write('%s\t%s\n'%(key,val))
    f.close()


tag = all_parameters[vary_parameter][0].split('=')[0]
parameter = generateParameters()

for common,fileData in parameter:
    data = read_data(fileData)
    for x in xval:
        if( not data.has_key(x) ):
            print common, 'does not contain',xlabel,x
        else:
            header = '#%s\t%s\n'%(tag,ylabel)
            filename = '%s=%s'%(xlabel,x)
            outfile = common[:]
            outfile.insert(vary_parameter,filename)
            outfile ='_'.join(outfile) + '.txt'
            print 'writing :',outfile
            writeFile(outfile,header,data[x])

raw_input('\n\nPress enter to exit!')
