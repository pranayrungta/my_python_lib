import os

def sortedList(paraDic):
    return [paraDic[i]  for i in sorted(paraDic)]

def dicToParaValues(paraDic, para):
    dic = paraDic.copy()
    for key,value in dic.items():
        dic[key] = para[key][value]
    return dic

def outfolder(out_folder, all_parameters, vary_parameter):
    if(out_folder=='None'): folderName = './'
    elif(out_folder=='auto'):
        folderName = all_parameters[vary_parameter][0]
        folderName = 'varying ' + folderName.split('=')[0]
    else: folderName = out_folder
    if(not os.path.isdir(folderName) ):
        os.mkdir(folderName)
    return folderName

def title_outfile(paraDic, para, out_folder):
    values = sortedList( dicToParaValues(paraDic,para) )
    title =  ' '.join(values)
    outfile =  '_'.join(values)
    if(out_folder!='./'): outfile=out_folder+'/'+outfile
    return title,outfile

# here vary is index of (varying parameter -> curve)
def filename_curve(parameters,paraDic,vary):
    valueDic = dicToParaValues(paraDic,parameters)
    curve = valueDic[vary]
    filename = sortedList(valueDic)
    filename = '_'.join(filename)+ '.txt'
    return filename,curve

def check_validity(fileData):
    valid_files = []
    for filepath,vary in fileData:
        if(os.path.isfile(filepath)):
            valid_files += [(filepath, vary)]
        else: print('File not found : ',filepath)
    return valid_files

#------------------FILE PATH-----------------------
def raw_file_path(filename,root):
    filepath = '/'.join([root,filename])
    return filepath

def lib_file_path(filename,root):
    filepath = filename.split('_')[:-1]
    filepath = '/'.join(filepath)
    filepath = '/'.join([root,filepath, filename])
    return filepath

def file_path_method(fileStructure):
    if(fileStructure=='raw'):
        return raw_file_path
    elif(fileStructure=='lib'):
        return lib_file_path
    else: raise ValueError('unknown fileStructure')
#---------------------------------------------------

#-----generating filenames------------
# format :  list of  [     outfile, title,
#                       [(filepath1, vary1),
#                        (filepath2, vary2), ]
#                    ]
def parameter_generator(all_parameters,vary_parameter,for_all_fixed,
                        constant_parameter, base, fileStructure,
                        out_folder='./'): # for backward compatibility
    file_path = file_path_method(fileStructure)
    out_folder = outfolder(out_folder,all_parameters,vary_parameter)
    no_of_files = len(all_parameters[for_all_fixed])
    plots_per_file = len(all_parameters[vary_parameter])

    parameter=[]
    # fileNo = output file no.
    for fileNo in range(no_of_files):
        paraDic = constant_parameter.copy()

        paraDic[for_all_fixed]= fileNo
        title,outfile = title_outfile(paraDic,all_parameters,out_folder)

        fileData = []
        for curveNo in range(plots_per_file):
            paraDic[vary_parameter] = curveNo
            filename,curve=filename_curve(all_parameters, paraDic, vary_parameter)
            filepath = file_path(filename,base)
            fileData += [ (filepath, curve) ]
        fileData = check_validity(fileData)
        if(len(fileData)>0):
            parameter += [ [outfile,title, fileData] ]
    return parameter

def display(valid_file_blocks):
    print('valid_file_blocks=\\')
    import pprint
    pp = pprint.PrettyPrinter(indent=4,width=120)
    pp.pprint(valid_file_blocks)
