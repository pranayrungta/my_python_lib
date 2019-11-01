# Files should satisfy the following criteria
criteria = ['.txt']
nonCriteria = ['$']

base='./'
fileStructure = 'raw' # 'raw' 'lib'

replaceLines = {'\n':'\n\n',}
#----------------------------------------------


def exactReplace(filename, repDic):
    lines = open(filename , 'r').readlines()
    for i,line in enumerate(lines):
        if(line in repDic):
            lines[i] = repDic[line]
    return ''.join(lines)

import Pranay.files_structure.criteria as fileGen
files = fileGen.files(criteria, nonCriteria, base, fileStructure)
for filename,root in files:
    print('-----------%s----------'%filename)
    #print( open(filename,'r').read() )
    print('-----------replaced %s----------'%filename)
    #print( exactReplace(filename,replaceLines) )
    



