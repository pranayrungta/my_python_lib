
def raw_file_path(filename,root):
    filepath = '/'.join([root,filename])
    return filepath


def lib_file_path(filename,root):
    filepath = filename.split('_')[:-1]
    filepath = '/'.join(filepath)
    filepath = '/'.join([root,filepath, filename])
    return filepath


def all_raw_files(root):
    import os
    files = [filename for filename in os.listdir(root)]
    files = [(filename,(root+'/'+filename))
             for filename in files]
    files = [(filename,filepath)
             for filename,filepath in files
             if os.path.isfile(filepath)]
    return files

def all_lib_files(root):
    import os
    all_files = []
    for root,fol,files in os.walk(root):
        for filename in files:
            all_files += [(filename,(root+'/'+filename))]
    return all_files
