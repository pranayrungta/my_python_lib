from __main__ import *
#-----maintaining backward compatibility----
try: out_folder 
except NameError: out_folder='auto'
#---------generate filenames------------
import Pranay.files_structure.filenameGen as fileGen
from Pranay.gnuplotter.gnuplotter_basic import *

def power_law_fit_cmd(filepath, vary, usingColms):
    colms = '%s:%s'%usingColms
    tag = vary.split('=')[-1]
    line1 = "f%s(x) = a%s*x**b%s  \n"%((tag,)*3)
    line2 = "fit f%s(x) '%s' u %s via a%s, b%s  \n"%(tag,filepath,colms,tag,tag)
    line3 = "title_f%s(a%s,b%s) = "%((tag,)*3)
    label = "sprintf(  'f(x) = %.2f (x^{%.2f}) "
    bval = ' for %s '%vary
    end = "', a%s, b%s   ) \n"%(tag, tag)
    line3 += label + bval + end
    return line1+line2+line3

def plotClause(filepath,vary):
    tag = vary.split('=')[-1]
    s = ', f%s(x) title title_f%s(a%s,b%s) '%((tag,)*4)
    return filenameClause(filepath,vary)+s

def fit_files(fileData,usingColms,fit):
    if(fit=='power'): fit_cmd=power_law_fit_cmd
    else: raise ValueError('program under construction!!!')
    return '\n'.join( fit_cmd(filepath,vary,usingColms)
                      for filepath,vary in fileData )

def plotBlock(fileData):
    return '\n'.join([
     fit_files(fileData,using_colms,fit),
     plotStatement(fileData,plotClause)  ])


#------------main program-------------------
valid_file_blocks = fileGen.parameter_generator(all_parameters,vary_parameter,
                for_all_fixed,constant_parameter,base,fileStructure,out_folder)

if(len(valid_file_blocks)==0):
    print '\nNo files to be plotted'
else:
    script = open('script.plt', 'w')
    scriptHead(script)
    for outfile, title, fileData in valid_file_blocks:
        script.write( 'set output "%s.%s" \n'%(outfile,ext) )
        script.write( 'set title "%s" \n\n'%title )
        script.write( plotBlock(fileData) )
        script.write( '\n\n' )
    script.write( '\n' )
    script.write( 'unset output ; exit gnuplot \n' )
    script.close()

    if(plot):
        import os
        os.system('gnuplot script.plt')
        os.remove('script.plt')
#-----------------------------------------
