import os, fnmatch

def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append([os.path.join(root, name), name])
    return result

def main(fetch_parameters):
    for parameters in fetch_parameters:
        filename = '_'.join(parameters) + '.txt'

        for oldpath,newpath in find(filename, '.'):
            os.rename(oldpath,newpath)

