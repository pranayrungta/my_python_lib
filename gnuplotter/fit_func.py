#---------------power_law_fit-------------------------
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

#--------------------------------------------------

def fit_files(fileData,usingColms,fit):
    if(fit=='power'):
        fit_cmd=power_law_fit_cmd
    elif(fit=='linear'):
        print 'program under construction!!!'
        raw_input('Press enter to exit!!!')
        exit()
    s=''
    for filepath,vary in fileData:
        s+=fit_cmd(filepath,vary,usingColms)
        s+='\n'
    return s

def plot_fitCurve_clause(vary):
    tag = vary.split('=')[-1]
    s = 'f%s(x) title title_f%s(a%s,b%s) '%((tag,)*4)
    return s

