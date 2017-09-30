from __main__ import *

import Pranay.files_structure.filenameGen as fileGen
try: valid_file_blocks
except NameError: valid_file_blocks=fileGen.parameter_generator(
    all_parameters,vary_parameter,for_all_fixed,
    constant_parameter, base, fileStructure, out_folder )

import Pranay.gnuplotter.gnuplotter_basic as plt
def power_law_fit_cmd(filepath, vary):
    tag = vary.split('=')[-1]
    line1 = "f%s(x) = a%s*x**b%s  \n"%((tag,)*3)
    line2 = "fit f%s(x) '%s' u %s via a%s, b%s \n"%(tag,filepath,plt.colm,tag,tag)
    line3 = "title_f%s(a%s,b%s) = "%((tag,)*3)
    line3 += "sprintf(  'f(x) = %.2f (x^{%.2f}) " #label
    line3 += " for %s  ', a%s, b%s   ) \n"%(vary, tag, tag)
    return line1+line2+line3

def fit_files(fileData,fit):
    if(fit=='power'): fit_cmd=power_law_fit_cmd
    else: raise ValueError('program under construction!!!')
    plt.script.write( '\n'+ '\n'.join(fit_cmd(filepath,vary)
                             for filepath,vary in fileData) + '\n')
def filenameClause(filepath,vary):
    tag = vary.split('=')[-1]
    s = ', f%s(x) title title_f%s(a%s,b%s) '%((tag,)*4)
    return plt.filenameClause(filepath,vary)+s

if( len(valid_file_blocks)==0 ):
    print('No files to be plotted')
elif(terminal=='display_files'):
    fileGen.display(valid_file_blocks)
else:
    plt.initialize(terminal,set_grid, plot_With, using_colms)
    plt.setAxis(xlabel,ylabel,xRange,yRange,xRangeflag,yRangeflag)
    for outfile, title, fileData in valid_file_blocks:
        plt.output(outfile,title)
        fit_files(fileData,fit)
        plt.plot(fileData,filenameClause)
    plt.draw(plot)
