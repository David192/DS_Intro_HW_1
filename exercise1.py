#A

def my_func(x1, x2, x3):
    check_float_x1 = isinstance(x1, float)
    check_float_x2 = isinstance(x2, float)
    check_float_x3 = isinstance(x3, float)
    try:
       if(x1 + x2 + x3) == 0:
          return "Not a number – denominator equals zero"
       elif check_float_x1 == False | check_float_x2 == False | check_float_x3 == False:
          return "Error: parameters should be float"
       else:
          return ((x1+x2+x3)*(x2+x3)*x3)/(x1+x2+x3)
    except SystemError:
        return None

#B

def convert(hours, minutes):
    if hours > 0 or minutes > 0:
        return hours*3600 + minutes*60
    else:
        return "Input error!"

