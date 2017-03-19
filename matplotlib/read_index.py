import pylab

def get_blocks(filename):
    with open(filename , 'r') as f:
        blocks = f.read().strip()
    blocks =[line.strip() for line in blocks.split('\n')]
    blocks = '\n'.join(blocks)
    blocks = blocks.split('\n\n\n')
    return blocks

def header_data(block):
    block = block.split('\n')
    for i,line in enumerate(block):
        if(line[0]!='#') :
            header = block[i-1][1:]
            block = block[i:]
            break
    header = [s.strip() for s in header.split('\t')]
    block = pylab.array([pylab.array([float(num)
                        for num in row.strip().split('\t')])
                        for row in block ] )
    return header,block
