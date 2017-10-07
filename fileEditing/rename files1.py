import os
s= 'RandomScaleFree'
for root,dire, files in os.walk('./'):
    if(len(files)>0):
        for filename in files:
            if('.txt' in filename):
                new = filename.split('_')[1:]
                new = [s]+new
                new = '_'.join(new)
                filename = os.path.join(root,filename)
                new = os.path.join(root,new)
                print filename
                print new
                print
                #os.rename(filename,new)
