from __main__ import *


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

def filenameClause(filepath, curve_title):
    colm= '%s'%using_colms[0]
    for i in using_colms[1:]:
        colm+= ':%s'%i
    s =  '"%s" u %s '%(filepath,colm)
    s += 'w %s title "%s" '%(plot_With,curve_title)
    return s

def plotStatement(fileData,plotClause):
    clauses = [plotClause(filepath,curve_title)
          for filepath,curve_title in fileData ]
    clauses[0] = 'plot '+ clauses[0]
    clauseSep = ', \t \\\n     '
    return clauseSep.join(clauses)
