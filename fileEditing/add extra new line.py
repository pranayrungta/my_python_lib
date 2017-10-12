# Files should satisfy the following criteria
criteria = ['.txt']
nonCriteria = ['$']

replaceLines = {'\n':'\n\n',}
base='./'



#----------------------------------------------
import criteria as ct
import replace as rp

fileData = ct.rawFiles(base,criteria,nonCriteria)
for filename,filepath in fileData:
    print('-----------%s----------'%filename)
    #print( open(filename,'r').read() )
    print('-----------replaced %s----------'%filename)
    #print( rp.exactReplace(filename,replaceLines) )
    



