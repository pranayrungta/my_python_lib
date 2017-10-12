# This program replaces text in text files
# inside all folders in current working directory
# satisfying th file criteria
criteria = ['.py']
nonCriteria = ['.pyc']

base = './../'
fileStructure = 'lib' # 'raw' 'lib'
#-----------------------------------------

look_for = 'criteria'
replace_with = ''
print_format = 'idle-python3.5 "$"'

#1. Show filenames
#2. Show file + contents
#3. Show replaced contents
#4. apply replacement
action = 1




#----------main program-----------
import os
import Pranay.files_structure.criteria as fileGen
files = fileGen.files(criteria, nonCriteria, base, fileStructure)

for filename,root in files:
    filepath = os.path.join(root,filename)
    data = open(filepath, 'r').read()
    if(look_for in data):
        if(action==1):
            print( print_format.replace('$',filepath) )
        elif(action==2):
            print('===========================')
            print(filepath)
            print('===========================')
            print( data )
            print('---------xxxxxxx-----------')
        elif(action==3):
            print('===========================')
            print(filepath)
            print('===========================')
            print( data.replace(look_for,replace_with) )
            print('---------xxxxxxx-----------\n\n')
        elif(action==4):
            print('applying change to : ', filepath)
            f = open(filepath,'w')
            f.write( data.replace(look_for,replace_with) )
            f.close()
input('\n\nPress enter to exit...')
