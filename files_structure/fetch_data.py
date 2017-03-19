from __main__ import*

import os, fnmatch
def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append([os.path.join(root, name), name])
    return result



for parameters in fetch_parameters:
    filename = '_'.join(parameters) + '.txt'

    s= find(filename, '.')
    for i in s:
        os.rename(i[0],i[1])

