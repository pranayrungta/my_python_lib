def addline(filename, newfilename):
    f = open(filename , 'r')
    fout = open( newfilename, 'w')
    for line in f:
        fout.write(line)
        if (line == '\n'):
            fout.write('\n')
    f.close()
    fout.close()
        





import os
ls = os.listdir('./')
files = [i for i in ls if ('.txt' in i and os.path.isfile(i) ) ]
for filename in files:
    addline(filename,'xy'+filename)



