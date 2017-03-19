from __main__ import *
from read_index import *

pylab.figure(figsize=canvas)
#============ Plotting===================
pylab.xlabel(xlabel[0],fontsize=xlabel[1])
pylab.ylabel(ylabel[0],fontsize=ylabel[1])

if(xRangeflag == True): pylab.xlim(xRange)
if(yRangeflag == True): pylab.ylim(yRange)

if(logx):pylab.xscale('log')
if(logy):pylab.yscale('log')

blocks = get_blocks(filename)

cm = pylab.cm.get_cmap(color_map)
for index,(x,y,z),label in plot_details:
    header,data  = header_data(blocks[index])
    pylab.scatter( data[:,x], data[:,y], c=data[:,z],
                   vmax = 10, vmin = 0, cmap = cm, label=label,
                   marker=marker, s=markerSize, alpha=opacity)

if(colorBar): pylab.colorbar()
for text_label in text_labels:
    pylab.text( *text_label, fontsize = fontSize)

if(output_format=='show'): pylab.show()
else: pylab.savefig('%s.%s'%(outfilename,output_format))    
pylab.close()
