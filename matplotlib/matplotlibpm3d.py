from __main__ import *


import pylab

def labels(tag):
    yl,xl = tag.split('\\')
    if(xlabel!='auto'):
        xl=xlabel
    if(ylabel!='auto'):
        yl=ylabel
    return yl,xl

def set_title(filename):
    if(title=='auto'):
        pylab.title(filename[:-4])
    elif(title!=None):
        pylab.title(title)

def spacetime_data(filename):
    with open(filename,'r') as f:
        content = f.read()
    content = content.strip()
    content = content.split('\n')
    content = [i.strip() for i in content]
    content = [i.split('\t') for i in content]

    #label = content[0][0]
    ylabel,xlabel = labels(content[0][0])
    x=[ float(i) for i in content[0][1:] ]
    x = pylab.array(x)
    content = [[float(i) for i in line] for line in content[1:]]
    content = pylab.array(content)
    y = content[:,0]
    content = content[:,1:]
    return (x,xlabel),(y,ylabel),content

def pm3dplot(filename):
    (x,xlabel),(y,ylabel),z = spacetime_data(filename)
    if(vertical_on_x):
        (x,xlabel),(y,ylabel)= (y,ylabel),(x,xlabel)
        z = z.T
    if(colorRange=='auto'):
        pylab.imshow(z, aspect='auto', origin='lower',
                 interpolation = 'none',
                 extent=(x.min(),x.max(),y.min(),y.max())
                 )
    else:
        pylab.imshow(z, aspect='auto', origin='lower',
                 interpolation = 'none',
                 extent=(x.min(),x.max(),y.min(),y.max()),
                 vmin=colorRange[0], vmax=colorRange[1]
                 )

    if(xRange!='auto'):pylab.xlim(xRange[0],xRange[1])
    if(yRange!='auto'):pylab.ylim(yRange[0],yRange[1])
    
    set_title(filename)
    pylab.xlabel(xlabel)
    pylab.ylabel(ylabel)
    pylab.colorbar()
    if(output=='show'):
        pylab.show()
    else:
        pylab.savefig('%s.%s'%(filename[:-4],output))
    pylab.close()




import os
ls=  os.listdir('./')
files = [ filename for filename in ls if(
                all(crit in filename for crit in criteria)
                and os.path.isfile(filename) ) ]
for filename in files:
    print('Plotting :',filename)
    pm3dplot(filename)
print('\nDone !')
