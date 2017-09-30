files =\
[
    ]


line_before = 'fileStructure'
line_after = '#-----gnuplot'
insertLine = "out_folder = 'auto' # 'FOLDER' 'None' \n"

def FirstLineIndex(lines):
   for i in range(len(lines)):
      if( lines[i].strip().startswith(line_before) ):
         return i
      
def insert_line(filename):
   lines = open(filename, 'r').readlines()

   i = FirstLineIndex(lines)+1
   while(i<len(lines)):
      if(lines[i].strip()==''):i=i+1
      elif(lines[i].strip().startswith(line_after) ):
         lines.insert(i,insertLine)
         print('====================')
         print(''.join(lines[i-3:i+3]))
         print('====================')
         return ''.join(lines)
      else:
         print("Other non-empty line exist\n")
         return False
   
import os
Menu =\
'''1.Replace and Display  2.Skip 3.Apply Change
Choice(1/2/3):'''

changed = []
skiped = []
for filename in files:
   print('\n\n\n\n================\n\n\n\n')
   print(filename)
   print(open(filename,'r').read())
   choice = input(Menu)
   while(choice!='2'):
       if(choice=='1'):
           replaced=insert_line(filename)
       elif(choice=='3'):
           replaced=insert_line(filename)
           confirm = input('Sure (y/n)?')
           if(confirm=='y'):
              #os.rename(filename, filename+'.backup')
              f=open(filename,'w')
              f.write(replaced)
              f.close()
              changed += [filename]
              break
           else: print('enter again...')
       choice = input(Menu)
   if(choice=='2'): skiped += [filename]

import pprint
p=pprint.PrettyPrinter(indent=4, width=200)
print('changed=\\')
p.pprint(changed)
print('skiped=\\')
p.pprint(skiped)
print('done')
                

