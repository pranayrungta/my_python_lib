def supply_data(filename):
    f= open(filename, 'r')
    s=f.readline()
    while(s[0]=='#'):
        buf = s
        s=f.readline()
    buf = buf.strip().split('\t')
    data = []
    data += [buf]
    while(s!='' and s!='\n' ):
        s=s.strip().split('\t')
        data += [s]
        s = f.readline()
    f.close()
    return data


def writeTranspose(data, outfile) :
    data[0][0] = '# p\\b '
    rows = len(data)
    colm = len(data[0])

    f = open(outfile, 'w')
    for i in range(colm):
        for j in range(rows):
            f.write( '%s\t'%data[j][i])
        f.write('\n')
    f.close()


def Transpose(infile, outfile):
    data = supply_data(infile)
    writeTranspose(data, outfile)
