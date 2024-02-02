from main import *
from sir import *


'''
In order to find the maximum of the curve I, we need to find where its first 
derivative is zero.
Need to define the two functions you will feed to your newton method
'''


def dIdt(t):  
    ##need to calculate S(t) and I(t) first
    St, It, Rt = sir(init, t, R0)
    ## then use formula for dIdt: R0SI - I
    return R0*St*It - It
'''
    Current issues in the function:
    need to define init, R0, since these are
    not imported from sir.py since they're under 
    __main__ block.

    You can define them globally 
    or, best,
    rewrite your Newton method in such a way so that 
    you can specifiy init and R0 everytime you call the function.
'''
    

def dI2dt2(t):
    return