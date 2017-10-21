from __main__ import *

import Pranay.files_structure.filenameGen as fileGen
try: valid_file_blocks
except NameError: valid_file_blocks=fileGen.parameter_generator(
    all_parameters,vary_parameter,for_all_fixed,
    constant_parameter, base, fileStructure, out_folder )

import Pranay.gnuplotter.gnuplotter_basic as plt
def power_law_fit_cmd(filepath, vary):
    tag = vary.split('=')[-1]
    f,a,b = f'f{tag}', f'a{tag}', f'b{tag}'
    line1 = f"{f}(x) = {a}*x**{b}\n"
    line2 = f"fit {f}(x) '{filepath}' u {plt.colm} via {a}, {b}\n"
    line3 = ( f"title_{f}({a},{b}) = sprintf( 'f(x) = "+
              r"%.2f (x^{%.2f}) for " + f"{vary}',{a},{b} ) \n" )
    return line1+line2+line3

def fit_files(fileData,fit):
    if(fit=='power'): fit_cmd=power_law_fit_cmd
    else: raise ValueError('program under construction!!!')
    plt.script.write( '\n'+ '\n'.join(fit_cmd(filepath,vary)
                             for filepath,vary in fileData) + '\n')
def filenameClause(filepath,vary):
    tag = vary.split('=')[-1]
    f,a,b = f'f{tag}', f'a{tag}', f'b{tag}'
    s = f', {f}(x) title title_{f}({a},{b}) '
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
        plt.script.write('\n')
    plt.draw(plot)
