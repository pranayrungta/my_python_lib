from __main__ import *

if(iteractive):
    import matplotlib
    matplotlib.interactive(True)
import numpy as np
import matplotlib.pyplot as plt

def get_blocks(filename):
    blocks = open(filename , 'r').read().strip()
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
    block = np.array([np.array([float(num)
                        for num in row.strip().split('\t')])
                        for row in block ] )
    return header,block

def printNewpos(annotate):
    new = []
    for i in annotate:
        new+= [ (i.get_text(), i.get_position()) ]
    import pprint
    pp= pprint.PrettyPrinter(indent=4)
    pp.pprint(new)

#============ Plotting===================
plt.xlabel(*xlabel);plt.ylabel(*ylabel)
plt.xlim(*xlim);plt.ylim(*ylim)

if('x' in log):plt.xscale('log')
if('y' in log):plt.yscale('log')

blocks = get_blocks(filename)

for index,(x,y),label in plot_details:
    header,data  = header_data(blocks[index])
    plt.plot( data[:,x], data[:,y], label=label,**plot_with)
##    print label
##    for i,t in enumerate(data[:,x]):
##        print '[ %s, %s,'%(t, data[:,y][i])
##    print

if(legend):plt.legend()
annotate = []
for x,y, label in text_labels:
    annotate+= [plt.annotate(label, (x,y))]
plt.tight_layout()
if(output_format=='show'):
    if(iteractive):
        for i in annotate:
            i.draggable()
    plt.show()
else: plt.savefig('%s.%s'%(outfilename,output_format))
plt.close()
