criteria = ['.txt','dynamic']
tag = r'time\space'


def dataDic(filename):
    data = {}
    with open(filename, 'r') as f:
        line = f.readline().strip()
        while(line[0]=='#'):
            line = f.readline().strip()
        while(line!=''):
            values = line.strip().split('\t')
            if(len(values)==3):
                values = [float(value.strip()) for value in values]
                t,x,value = values
                if t not in data:
                    data[t] = {}
                data[t][x] = value
            line = f.readline()
    return data

def writeData(filename):
    data = dataDic(filename)
    f = open('%s.spt'%filename[:-4], 'w')
    f.write(tag)
    elem=next( iter(data.values()) )

    for header in sorted(elem):
        f.write('\t%s'%header)
    f.write('\n')

    for t,xval in sorted(data.items()):
        f.write(str(t))
        for x,value in sorted(xval.items()):
            f.write('\t%s'%value)
        f.write('\n')
    f.write('\n')
    f.close()


if __name__ == "__main__":
    import os
    ls=  os.listdir('./')
    files = [ filename for filename in ls if(
              all(crit in filename for crit in criteria)
                  and os.path.isfile(filename) ) ]
    for filename in files:
        print('Converting :',filename)
        writeData(filename)
    input('\nDone ! Press enter to exit')
