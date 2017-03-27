from __main__ import *
from Pranay.matplotlib.read_index import *

#============ Plotting===================
pylab.xlabel(xlabel[0],fontsize=xlabel[1])
pylab.ylabel(ylabel[0],fontsize=ylabel[1])

if(xRangeflag == True): pylab.xlim(xRange)
if(yRangeflag == True): pylab.ylim(yRange)

if(logx):pylab.xscale('log')
if(logy):pylab.yscale('log')

blocks = get_blocks(filename)

for index,(x,y),label in plot_details:
    header,data  = header_data(blocks[index])
    pylab.plot( data[:,x], data[:,y], label=label,marker=marker,
                linestyle=linestyle,  markersize=markerSize)
##    print label
##    for i,t in enumerate(data[:,x]):
##        print '[ %s, %s,'%(t, data[:,y][i])
##    print
                           
if(legend):pylab.legend() 
for text_label in text_labels:
    pylab.text( *text_label, fontsize = fontSize)

if(output_format=='show'): pylab.show()
else: pylab.savefig('%s.%s'%(outfilename,output_format))    
pylab.close()
