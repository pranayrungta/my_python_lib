from __main__ import *

#---------generate filenames------------
if(fileStructure=='raw'):
    from Pranay.files_structure.filepath import all_raw_files as file_path
elif(fileStructure=='lib'):
    from Pranay.files_structure.filepath import all_lib_files as file_path
#-----------------------------------------

def gentitle(filename):
    name = filename.split('.')[0]
    titleName = name.split('_')
    return ' '.join(titleName)

import os
def check_validity(fileData):
    valid_files = []
    for filepath,title in fileData:
        if(os.path.isfile(filepath)):
            valid_files += [(filepath, title)]
        else :
            print 'File not found : ',filepath
    return valid_files

def select(all_files,criteria,nonCriteria):
    return [ (filepath,filename) for (filepath,filename) in all_files
             if( all(crit in filename for crit in criteria)
                 and not all(crit in filename for crit in nonCriteria)
               ) ]

#-----generating filenames------------
# format :  list of  [     outfile, title,
#                       [(filepath1, vary1),
#                        (filepath2, vary2), ]
#                    ]
def parameter_generator_individual(all_files):
    parameter=[]
    for i,(filename,filepath) in enumerate(all_files):
        outfile = filename[:-4]
        title = gentitle(outfile)
        fileData = [(filepath,'')]
        fileData = check_validity(fileData)
        if(len(fileData)>0):
            parameter += [ [outfile,title, fileData] ]
    return parameter

def parameter_generator_together(all_files,criteria,outfile):
    if(outfile=='auto'):outfile = '_'.join(criteria[1:])
    title = gentitle(outfile)
    fileData = []
    for i,(filename,filepath) in enumerate(all_files):
        fileData += [( filepath,gentitle(filename) )]
    fileData = check_validity(fileData)
    if(len(fileData)>0):
        parameter = [ [outfile,title, fileData] ]
    return parameter
#-----------------------------------------------------------


all_files = file_path(base)
valid_file_blocks=[]
for i,(plot_type, crit, non_crit) in enumerate(all_parameters):
    files = select(all_files,crit,non_crit)
    if(plot_type[0]=='together'):
        valid_file_blocks += parameter_generator_together(files,crit,plot_type[1])
    elif(plot_type[0]=='individual'):
        valid_file_blocks += parameter_generator_individual(files)
    else:
        print 'wrong plot_type :',plot_type
        print 'check index :',i

#------------main program-------------------
from Pranay.gnuplotter.gnuplotter_basic import *
def plotBlock(fileData):
    return plotStatement(fileData,filenameClause)

if(len(valid_file_blocks)>0):
    generate_script(valid_file_blocks,'.',plotBlock)

    if(plot):
        os.system('gnuplot script.plt')
        os.remove('script.plt')
else:
    print '\nNo files found'
#-----------------------------------------
