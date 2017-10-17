def initialize(terminal, set_grid, plot_With, using_colms=[]):
    global script, ext, colm, plot_with

    if(terminal=='jpeg')  : ext = 'jpg'
    elif(terminal=='png') : ext = 'png'
    elif(terminal=='show'): ext = 'show'
    elif(terminal=='eps'):
        ext = 'eps'
        terminal = 'postscript enhanced color font "Helvetica,24"'

    script = open('script.plt', 'w')
    if(ext!='show'):script.write( f'set terminal {terminal}\n\n')
    if(set_grid): script.write( 'set grid \n\n' )

    colm=':'.join(str(i) for i in using_colms)
    plot_with = plot_With

def setAxis(xlabel,ylabel,xRange,yRange,xRangeflag,yRangeflag):
    script.write(f'set xlabel "{xlabel}"\n')
    script.write(f'set ylabel "{ylabel}"\n')
    script.write( '\n' )
    if(xRangeflag==True):script.write('set xrange [%s:%s]\n'%xRange )
    if(yRangeflag==True):script.write('set yrange [%s:%s]\n'%yRange )
    script.write( '\n' )

def output(outfile, title):
    if(ext!='show'):script.write(f'set output "{outfile}.{ext}"\n')
    script.write(f'set title "{title}"\n')

def filenameClause(filepath, curve_title):
    return  f'"{filepath}" u {colm} w {plot_with} title "{curve_title}"'

def plot(fileData, plotClause=filenameClause):
    clauses = [plotClause(filepath,curve_title)
                  for filepath,curve_title in fileData ]
    clauses[0] = 'plot ' + clauses[0]
    clauseSep = ', \t \\\n     '
    script.write(clauseSep.join(clauses)+'\n\n')

def draw(plot):
    script.write('\n')
    script.write('unset output ; exit gnuplot \n')
    script.close()
    if(plot):
        import os
        if(ext=='show'):os.system('gnuplot -p script.plt')
        else: os.system('gnuplot script.plt')
        os.remove('script.plt')
