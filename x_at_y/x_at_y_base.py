import numpy

# function searches for threshold fnode
# and return not_found if not found
def xCrit_value(filepath,threshold,not_found,colms):
    col0,col1 = colms
    data = numpy.loadtxt(filepath)
    for i in range(1,len(data)):
        if( (data[i-1][col1]-threshold)*
            (data[i][col1]  -threshold) < 0 ):
            return data[i][col0]
    return not_found


#format of fileData = [ (filepath1,vary1),
#                    (filepath2,vary2),]
def x_at_yList(fileData,threshold,not_found,colms):
    values = {}
    for filepath,vary in fileData:
        xAty = xCrit_value(filepath,threshold,not_found,colms)
        xval = float(vary.split('=')[-1])
        values[xval]= xAty
    return values

