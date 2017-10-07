from __main__ import *

if(interactive):
    import matplotlib
    matplotlib.interactive(True)
import matplotlib.pyplot as plt
import matplotlib as mpl; mpl.style.use('classic')
import numpy as np

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

def print_new_positions():
    new = []
    for i in annotate:
        new+= [ [i.get_position(), i.get_text()] ]
    import pprint
    pp= pprint.PrettyPrinter(indent=4)
    print('text_labels = \\')
    pp.pprint(new)

#============ Plotting===================
plt.xlabel(*xlabel);plt.ylabel(*ylabel)
plt.xlim(**xlim);plt.ylim(**ylim)

if('x' in log):plt.xscale('log')
if('y' in log):plt.yscale('log')

blocks = get_blocks(filename)
for index,(x,y),label in plot_details:
    header,data  = header_data(blocks[index])
    plt.plot( data[:,x], data[:,y], label=label,**plot_with)
if(legend):plt.legend()

annotate = []
for x,y, label in text_labels:
    annotate+= [plt.annotate(label, (x,y))]
    if(interactive):annotate[-1].draggable()

plt.tight_layout()
if(output_format=='show'): plt.show()
else: plt.savefig('%s.%s'%(outfilename,output_format))

if(not interactive):plt.close()
else:
    print('After changing positions of text_labels, call:')
    print('print_new_positions()')
    #print_new_positions()
