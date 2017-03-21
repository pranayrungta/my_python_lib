from __main__ import *



#-----terminal--------
if(terminal=='jpeg') : ext = 'jpg'
if(terminal== 'png') : ext = 'png'
if(terminal== 'eps')  :
    ext = 'eps'
    terminal = 'postscript enhanced color font "Helvetica,24"'
#----using colms-------
using_colms = '%s:%s:%s'%using_colms


f = open('script.plt' , "w")
f.write("set terminal %s\n"%terminal )
f.write("set pm3d map \n")
f.write("set xlabel '%s' \n"%xlabel)
f.write("set ylabel '%s' \n"%ylabel)
f.write("\n")

import os
ls= os.listdir('./')
files = [filename for filename in ls if(all(x in filename for x in criteria) )]
for filename in files:
    title = ' '.join( filename[0:-4].split("_") )
    f.write("set title '%s' \n"%title )
    f.write("set output '%s.%s'\n"%(filename[0:-4],ext) )
    f.write("splot '%s' using %s\n"%(filename, using_colms) )
    f.write("\n")
    f.write("\n")
f.write("unset output; exit gnuplot \n")
f.write("\n")
f.close()

if(plot):
    os.system('gnuplot script.plt')
    os.remove('script.plt')
