from __main__ import (terminal,
                      xlabel,xRangeflag,xRange,
                      ylabel,yRangeflag,yRange,
                      plot_With,using_colms,
                      set_grid)
import os

def filenameClause(filepath,curve_title):
    colm= '%s'%using_colms[0]
    for i in using_colms[1:]:
        colm+= ':%s'%i

    s =  '"%s" u %s '%(filepath,colm)
    s += 'w %s title "%s" '%(plot_With,curve_title)
    return s

def plotStatement(fileData,plotClause):
    filepath,curve_title = fileData[0]
    s = 'plot %s'%plotClause(filepath,curve_title)
    for filepath,curve_title in fileData[1:]:
        s+= ', \t \\\n     '
        s+= plotClause(filepath,curve_title)
    return s

#-----terminal--------
if(terminal=='jpeg') : ext = 'jpg'
if(terminal== 'png') : ext = 'png'
if(terminal== 'eps')  :
    ext = 'eps'
    terminal = 'postscript enhanced color font "Helvetica,24"'

def scriptHead(scriptfile):
    scriptfile.write( 'set terminal %s \n\n'%terminal )
    if(set_grid): scriptfile.write( 'set grid \n\n' )

    scriptfile.write( 'set xlabel "%s" \n'%xlabel )
    scriptfile.write( 'set ylabel "%s" \n'%ylabel )
    if(xRangeflag == True): scriptfile.write( 'set xrange [%s:%s] \n\n'%xRange )
    if(yRangeflag == True): scriptfile.write( 'set yrange [%s:%s] \n\n'%yRange )
    scriptfile.write( '\n' )


#------------------------------------------------------------
# parameter format - list of [   plotFilename_wihtout_ext,
#                                        curve_title,
#                               [ (filepath1, title1),
#                                 (filepath2, title2),  ]   ]
def generate_script(parameters,outFolder,plotBlock):
    script = open('script.plt', 'w')
    scriptHead(script)
    for outfile, title, fileData in parameters:
        script.write( 'set output "%s/%s.%s" \n'%(outFolder,outfile,ext) )
        script.write( 'set title "%s" \n'%title )
        script.write( plotBlock(fileData) )
        script.write( '\n\n' )
    script.write( '\n' )
    script.write( 'unset output ; exit gnuplot \n' )
    script.close()
#-----------------------------------------------------------------------
