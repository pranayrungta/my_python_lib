
def exactReplace(filename, repDic):
    lines = open(filename , 'r').readlines()
    for i,line in enumerate(lines):
        if(line in repDic):
            lines[i] = repDic[line]
    return ''.join(lines)


