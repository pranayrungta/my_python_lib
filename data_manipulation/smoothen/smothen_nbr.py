def processit(filename,setsize):
    f=open(filename , 'r')
    #getting data
    data=[]
    for line in f:
        x=line.split()
        x=[float(x[0]), float(x[1]), float(x[2])]
        data += [x]
        
    #making avg sets of setsize
    fl =open('smooth_nbr '+filename,'w')
    i=0
    while i+setsize<len(data):

        avgn =0.0
        avgx =0.0
        avgstd =0.0
        for index in range(i,i+setsize):
            avgn +=data[index][0]
            avgx +=data[index][1]
            avgstd +=data[index][2]
        nop= setsize
        avg = [avgn/nop, avgx/nop, avgstd/nop]
        fl.write('%.3f \t %0.6f \t %0.6f \n'%(avg[0],avg[1],avg[2]))

        i+=1
    fl.close()


import os
s = os.listdir(os.getcwd())
filelist=[]
for fn in s:
    if 'aoc' in fn:
        filelist+= [fn]

for i in filelist:
    processit(i,4)

