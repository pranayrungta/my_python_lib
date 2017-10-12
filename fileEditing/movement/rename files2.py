criteria= ['ScaleFree', 'order', '.txt']
s= 'DSF'

act = False #False True

import os
for root,dire, files in os.walk('./'):
    if(len(files)>0):
        for filename in files:
            if( all(crit in filename for crit in criteria) ):
                new = filename.split('_')[1:]
                new = [s]+new
                new = '_'.join(new)
                filename = os.path.join(root,filename)
                new = os.path.join(root,new)
                print filename
                print new
                print
                if(act): os.rename(filename,new)
