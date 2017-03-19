def lib_file_path(filename,root):
    filepath = filename.split('_')[:-1]
    filepath = '/'.join(filepath)
    filepath = '/'.join([root,filepath, filename])
    return filepath


def raw_file_path(filename,root):
    filepath = '/'.join([root,filename])
    return filepath
