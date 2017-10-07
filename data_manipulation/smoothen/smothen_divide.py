def processit(filename,setsize):
    f=open(filename , 'r')
    #getting data
    data=[]
    for line in f:
        x=line.split()
        x=[float(x[0]), float(x[1]), float(x[2])]
        data += [x]
        
    #making avg sets of setsize
    fl =open('smooth_divide '+filename,'w')
    i=0
    while i<len(data):

        limit=i+setsize
        if limit >len(data):
            limit=len(data)

        avgn =0.0
        avgx =0.0
        avgstd =0.0
        for index in range(i,limit):
            avgn +=data[index][0]
            avgx +=data[index][1]
            avgstd +=data[index][2]
        nop= len(range(i,limit))
        avg = [avgn/nop, avgx/nop, avgstd/nop]
        fl.write('%.3f \t %0.6f \t %0.6f \n'%(avg[0],avg[1],avg[2]))
        i+=setsize
    fl.close()


import os
s = os.listdir(os.getcwd())
filelist=[]
for fn in s:
    if 'aoc' in fn:
        filelist+= [fn]

for i in filelist:
    processit(i,4)
