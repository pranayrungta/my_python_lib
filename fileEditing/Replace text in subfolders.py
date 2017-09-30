# This program replaces text in text files
# inside all folders in current working directory
# satisfying th file criteria

filecriteria = ['','.py']
nonCriteria = ['.pyc','filenameGen.py','Replace']

look_for = "gnuplotter.gnuplotter"
replace_with = "out_folder"

#1. Show filenames
#2. Show file + contents
#3. Show replaced contents
#4. apply replacement
action = 1




#=====================================================================
import os

# return [flag, contents]
def criteria_satisfied(filepath):
    flags = [ (criteria in filepath) for criteria in filecriteria ]
    flags +=[ (criteria not in filepath) for criteria in nonCriteria]
    if(not all(flags) ):
        return [False,'']
    else:
        f= open(filepath, 'r')
        contents = f.readlines()
        f.close()

        for line in contents:
            if(look_for in line):
                return [True, contents]
        return [False,'']


def afterReplacement(contents):
    for i in range(len(contents)):
        if(look_for in contents[i]):
            contents[i] =  contents[i].replace(look_for,replace_with)
    return ''.join(contents)


#----------main program-----------
fileCollection = []
for root, directory, files in os.walk('./'):
    for filename in files:
        filepath = os.path.join(root,filename)
        isCriteriaSatisfied, contents = criteria_satisfied(filepath)
        if(isCriteriaSatisfied):
            if(action==1):
                print(filepath)
                fileCollection += [filepath]
            elif(action==2):
                print('===========================')
                print(filepath)
                print('===========================')
                print( ''.join(contents) )
                print('---------xxxxxxx-----------\n\n')
            elif(action==3):
                print('===========================')
                print(filepath)
                print('===========================')
                print(afterReplacement(contents))
                print('---------xxxxxxx-----------\n\n')
            elif(action==4):
                print('applying change to : ', filepath)
                f= open(filepath,'w')
                f.write(afterReplacement(contents))
                f.close()             
input('\n\nPress enter to exit...')
