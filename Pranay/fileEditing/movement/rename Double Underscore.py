import os

for root, directory, files in os.walk('./'):
    #print root
    for filename in files:
        filepath = os.path.join(root,filename)
        if('__' in filepath):
            print filepath
            new = filepath.replace('__', '_')
            print new
            print
            #os.rename(filepath, new)
            
