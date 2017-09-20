def initialize(terminal, set_grid, plot_With, using_colms=[]):
    global script, ext, colm, plot_with

    if(terminal=='jpeg') : ext = 'jpg'
    elif(terminal=='png'): ext = 'png'
    elif(terminal=='eps'):
        ext = 'eps'
        terminal = 'postscript enhanced color font "Helvetica,24"'
    elif(terminal=='show'):ext='show'
    script = open('script.plt', 'w')
    if(ext!='show'):script.write( 'set terminal %s \n\n'%terminal )
    if(set_grid): script.write( 'set grid \n\n' )

    colm=':'.join(str(i) for i in using_colms)
    plot_with = plot_With

def setAxis(xlabel,ylabel,xRange,yRange,xRangeflag,yRangeflag):
    script.write( 'set xlabel "%s" \n'%xlabel )
    script.write( 'set ylabel "%s" \n'%ylabel )
    if(xRangeflag == True): script.write( 'set xrange [%s:%s] \n\n'%xRange )
    if(yRangeflag == True): script.write( 'set yrange [%s:%s] \n\n'%yRange )
    script.write( '\n' )

def output(outfile, title):
    if(ext!='show'):
        script.write( 'set output "%s.%s" \n'%(outfile,ext) )
    script.write( 'set title "%s" \n'%title )    

def filenameClause(filepath, curve_title):
    return  '"%s" u %s w %s title "%s"'%(
        filepath, colm, plot_with, curve_title)

def plot(fileData, plotClause=filenameClause):
    clauses = [plotClause(filepath,curve_title)
          for filepath,curve_title in fileData ]
    clauses[0] = 'plot '+ clauses[0]
    clauseSep = ', \t \\\n     '
    script.write(clauseSep.join(clauses)+'\n\n')

def draw(plot):
    script.write( '\n' )
    script.write( 'unset output ; exit gnuplot \n' )
    script.close()
    if(plot):
        import os
        if(ext=='show'):os.system('gnuplot -p script.plt')
        else: os.system('gnuplot script.plt')
        os.remove('script.plt')
