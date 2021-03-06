def isFloat(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

def validTemp(**kwargs):
    """
    keyword arguments -> dict or list
    
    Returns dict of temperatures if all are valid else returns list of tempratures which are in error
    """
    T = {}
    error = []
    flag = True
    for key in kwargs:
        value = kwargs[key]
        if isFloat(value):
            t = float(value)
            if t >= -273.0 and t <= 3000.0:
                T[key] = t
            else:
                flag = False
                error.append("error" + key)
        else:
            flag = False
            error.append("error"+key)
    if flag:
        return T
    else:
        return error
            
