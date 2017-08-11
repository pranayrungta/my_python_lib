from __main__ import *

import matplotlib.pyplot as plt
import numpy as np

def labels(tag):
    yl,xl = tag.split('\\')
    if(xlabel!='auto'):
        xl=xlabel
    if(ylabel!='auto'):
        yl=ylabel
    return yl,xl

def set_title(filename):
    if(title=='auto'):
        plt.title(filename[:-4])
    elif(title!=None):
        plt.title(title)

def spacetime_data(filename):
    content = open(filename,'r').read()
    content = content.strip().split('\n')
    content = [i.strip().split('\t') for i in content]

    ylabel,xlabel = labels(content[0][0])
    x=[ float(i) for i in content[0][1:] ]
    x = np.array(x)
    content = [[float(i) for i in line] for line in content[1:]]
    content = np.array(content)
    y = content[:,0]
    content = content[:,1:]
    return (x,xlabel),(y,ylabel),content

def pm3dplot(filename):
    plt.figure(figsize=figsize)
    (x,xlabel),(y,ylabel),z = spacetime_data(filename)
    if(vertical_on_x):
        (x,xlabel),(y,ylabel)= (y,ylabel),(x,xlabel)
        z = z.T
    if(colorRange=='auto'): vmin_max = {}
    else: vmin_max = {'vmin':colorRange[0], 'vmax':colorRange[1]}
    plt.imshow(z, aspect='auto', origin='lower', interpolation = 'none',
                 extent=(x.min(),x.max(),y.min(),y.max()), **vmin_max )

    if(xRange!='auto'):plt.xlim(xRange[0],xRange[1])
    if(yRange!='auto'):plt.ylim(yRange[0],yRange[1])

    set_title(filename)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.colorbar()
    plt.tight_layout()
    if(output=='show'):
        plt.show()
    else:
        plt.savefig('%s.%s'%(filename[:-4],output))
    plt.close()




import os
ls=  os.listdir('./')
files = [ filename for filename in ls if(
                all(crit in filename for crit in criteria)
                and os.path.isfile(filename) ) ]
for filename in files:
    print 'Plotting :',filename
    pm3dplot(filename)
print '\nDone !'
