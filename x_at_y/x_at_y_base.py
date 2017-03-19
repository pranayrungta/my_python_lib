import numpy

# function searches for threshold fnode
# and return not_found if not found
def xCrit_value(filepath,threshold,not_found):
    data = numpy.loadtxt(filepath)
    for i in range(1,len(data)):
        if( (data[i-1][1]-threshold)*
            (data[i][1]  -threshold) < 0 ):
            return data[i][0]
    return not_found


#format of fileData = [ (filepath1,vary1),
#                    (filepath2,vary2),]
def x_at_yList(fileData,threshold,not_found):
    values = {}
    for filepath,vary in fileData:
        xAty = xCrit_value(filepath,threshold,not_found)
        xval = float(vary.split('=')[-1])
        values[xval]= xAty
    return values

