from __main__ import *

if(len(valid_file_blocks)==0):
    print '\nNo files to be plotted'
else:
    import Pranay.gnuplotter.gnuplotter_basic as plt
    plt.initialize(terminal,set_grid, plot_With, using_colms)
    plt.setAxis(xlabel,ylabel,xRange,yRange,xRangeflag,yRangeflag)
    for outfile, title, fileData in valid_file_blocks:
        plt.output(outfile,title)
        plt.plot(fileData)
    plt.draw(plot)
