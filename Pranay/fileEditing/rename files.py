# Files should satisfy the following criteria
criteria = ['.txt']
nonCriteria = ['$']

base='./'
fileStructure = 'raw' # 'raw' 'lib'
#------------------------------------------
def new_filename(filename):
    new = 'fil'+filename
    return new

    



import os
Menu =\
'''1.Display files 2.Replace and Display 3.Apply Change 4.Exit
Choice(1/2/3/4):'''

import Pranay.files_structure.criteria as fileGen
import pprint
p=pprint.PrettyPrinter(indent=4, width=130)


files = []; choice=''
while(choice!='4'):
    choice = input(Menu)
    if(choice=='1'):
        files = fileGen.files(criteria, nonCriteria, base, fileStructure)
        p.pprint(files)
        print()
    if(choice=='2'):
        if len(files)==0 :
            files = fileGen.files(criteria, nonCriteria, base, fileStructure)
        fileData=[]
        for filename,root in files:
            new=new_filename(filename)
            fileData.append([root,filename,new])            
        p.pprint(fileData)
        print()
    elif(choice=='3'):
        exists = []
        for root,filename,new in fileData:
            oldpath =os.path.join(root,filename)
            newpath =os.path.join(root,new)
            if(os.path.isfile(newpath)):
                exists.append([root,filename,new])
            else:
                os.rename(oldpath,newpath)
                print('old:',oldpath)
                print('new:',newpath)
                print()
        if(len(exists)>0):
            print('following files already exist:')
            p.pprint(exists)
            print('overwrite (y/n)?')
            break
            
        
##        
##       replaced=insert_line(filename)
##       confirm = input('Sure (y/n)?')
##       if(confirm=='y'):
##          #os.rename(filename, filename+'.backup')
##          f=open(filename,'w')
##          f.write(replaced)
##          f.close()
##          changed += [filename]
##          break
##       else: print('enter again...')
##    choice = input(Menu)
##    if(choice=='2'): skiped += [filename]
