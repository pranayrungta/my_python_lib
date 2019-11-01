# Files should satisfy the following criteria
criteria = ['b=','']
nonCriteria = [  '$' ]

# Whether existing folder should be deleted
overwrite = False  # True  False


# Destination folder name
folderName = 'b=-ve'    #' '.join(criteria)











import os, shutil
import criteria as ct
def movefiles():
    files = ct.rawFiles('./',criteria,nonCriteria)
    if os.path.isdir(folderName):
        if(overwrite):
            shutil.rmtree(folderName) # yes, remove old directory
            os.mkdir(folderName) # make new directory d
    else:        
        os.mkdir(folderName)

    for filename,root in files:
        os.rename(filename, folderName+'/'+filename)

movefiles()
