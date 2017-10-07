# Files should satisfy the following criteria
criteria = ['b=','']

nonCriteria = [  '$' ]

# Whether existing folder should be deleted
overwrite = False  # True  False


# Destination folder name
folderName = 'b=-ve'    #' '.join(criteria)











import os, shutil

def movefiles():
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

movefiles()
