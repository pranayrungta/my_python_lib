from __main__ import *

#---------generate filenames------------
if(fileStructure=='raw'):
    from Pranay.files_structure.filepath import raw_file_path as file_path
elif(fileStructure=='lib'):
    from Pranay.files_structure.filepath import lib_file_path as file_path
#-----------------------------------------

def gentitle(filename):
    name = filename.split('.')[0]
    titleName = name.split('_')
    return ' '.join(titleName)
    

def outfile_title(dic,index):
    if(dic['outfile']=='auto'):
        outfile = 'plot_'+str(index)
    else: outfile = dic['outfile']

    if(dic['title']=='auto'):
        title = gentitle(outfile)
    else: title = dic['title']

    return outfile,title

def infile_title(filetup):
    filename,title = filetup
    if(title=='auto'):
        title = gentitle(filename)
    return filename,title


import os
def check_validity(fileData):
    valid_files = []
    for filepath,title in fileData:
        if(os.path.isfile(filepath)):
            valid_files += [(filepath, title)]
        else :
            print('File not found : ',filepath)
    return valid_files


#-----generating filenames------------
# format :  list of  [     outfile, title,
#                       [(filepath1, vary1),
#                        (filepath2, vary2), ]
#                    ]
def parameter_generator(all_parameters, base, file_path):
    parameter=[]
    for i,(para,filelist) in enumerate(all_parameters):
        outfile,title = outfile_title(para,i)
        fileData = []
        for filetup in filelist:
            filename,curve = infile_title(filetup)
            filepath = file_path(filename,base)
            fileData += [(filepath,curve)]
        fileData = check_validity(fileData)
        if(len(fileData)>0):
            parameter += [ [outfile,title, fileData] ]
    return parameter
#-----------------------------------------------------------


##t= parameter_generator(all_parameters,base,file_path)
##for a,b,c in t:
##    print a
##    print b
##    for l,r in c:
##        print l,r
##    print 

from Pranay.gnuplotter.gnuplotter_basic import *
def plotBlock(fileData):
    return plotStatement(fileData,filenameClause)


#------------main program-------------------
valid_file_blocks = parameter_generator(all_parameters,base,file_path)
if(len(valid_file_blocks)>0):
    generate_script(valid_file_blocks,'.',plotBlock)

    if(plot):
        os.system('gnuplot script.plt')
        os.remove('script.plt')
else:
    print('\nNo files found')
#-----------------------------------------
