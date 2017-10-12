def isValid(filename, criteria=[''], nonCriteria=['$']):
    return ( all(crit in filename
                 for crit in criteria) and not 
             any(nonCrit in filename
                 for nonCrit in nonCriteria)  )

def display(data, variableName='valid_file_blocks'):
    import pprint
    pp = pprint.PrettyPrinter(indent=4,width=120)
    if(variableName.strip()!=''):
        print('%s=\\'%variableName)
    pp.pprint(data)

import os
def rawFiles(base='./', criteria=[''], nonCriteria=['$']):
    ls = os.listdir(base)
    fileData = []
    for filename in ls:
        filepath = os.path.join(base,filename)
        if( os.path.isfile(filepath) and
            isValid(filename,criteria,nonCriteria) ):
            fileData.append( (filename,base) )
    return fileData
              
def libFiles(base='./', criteria=[''], nonCriteria=['$']):
    valid=[]
    for root, directory, files in os.walk(base):
        valid += [ (filename,root) for filename in files
                    if isValid(filename,criteria,nonCriteria) ]
    return valid

def file_path_method(fileStructure):
    if(fileStructure=='raw'):
        return rawFiles
    elif(fileStructure=='lib'):
        return libFiles
    else: raise ValueError('unknown fileStructure')

def files(criteria, nonCriteria, base, fileStructure):
    file_path = file_path_method(fileStructure)
    return file_path(base,criteria,nonCriteria)
#-----------------------------------------------------------------
def outfolder(out_folder):
    if(out_folder=='None'): folderName = './'
    else:
        folderName = out_folder
        if( out_folder!='auto' and
            (not os.path.isdir(folderName)) ):
            os.mkdir(folderName)
    return folderName

def title_outfile(filename, root, folder):
    outfile = filename[0:-4]
    title =  ' '.join( outfile.split('_') )
    if(folder!='./'): outfile=folder+'/'+outfile
    return title,outfile

def parameter_generator(criteria, nonCriteria, base, fileStructure, out_folder):
    file_path = file_path_method(fileStructure)
    fileData = file_path(base,criteria,nonCriteria)
    folderName = outfolder(out_folder)

    valid_file_blocks = []
    for filename, root in fileData:
        if(folderName=='auto'):folder = root
        else:folder = folderName
        title, outfile = title_outfile(filename,root,folder)
        infile = os.path.join(root,filename)
        valid_file_blocks.append( (outfile,title,infile) )
    return valid_file_blocks
