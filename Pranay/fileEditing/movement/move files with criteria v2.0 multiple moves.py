# Files should satisfy the following criteria
criterialist = [('.txt', 'c=0.4'  ) ,
                ('.jpg', 'c=0.4'  ) ,

                ('.txt', 'c=0.15'  ) ,
                ('.jpg', 'c=0.15'  ) ,

                ('.txt', 'c=0.26'  ) ,
                ('.jpg', 'c=0.26'  ) ,

                ('.txt', 'c=1'  ) ,
                ('.jpg', 'c=1'  ) ,

                ]

nonCriteria = [  '$' ]

# Whether existing folder should be deleted
overwrite = False  # True  False











import os, shutil

def movefiles(folderName, criteria):
    ls = os.listdir('./')
    files = [i for i in ls if( all(x in i for x in criteria)
                            and not any(y in i for y in nonCriteria)
                            and os.path.isfile(i) ) ]

    if os.path.isdir(folderName):
        if(overwrite):
            shutil.rmtree(folderName) # yes, remove old directory
            os.mkdir(folderName) # make new directory d
    else:        
        os.mkdir(folderName)

    for filename in files:
        os.rename(filename, folderName+'/'+filename)
        #print filename , " : ", folderName+'/'+filename

for criteria in criterialist:
    folder = '_'.join(criteria[1:])
    #print folder
    movefiles(folder, criteria)
