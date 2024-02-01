import math

################################
####     MATH FUNCTIONS     ####
################################

def f0(x):
    return 2 * x - 1

def f1(x):
    return x**3 - 3*x + 1

def f2a(x):
    return x**2 - 2

def f2b(x):
    return x**2 - 3

def f3(x):
    return math.cos(x) - x

def f4(x):
    return f1(x)

def f5(x):
    return x**3 - 2*x + 2

def f6(x):
    return (math.exp(x) / (1+math.exp(x))) - 1/2

def f7(x):
    return math.sin(x) - x

def f8a(x):
    return abs(x)**(1/3)

def f8b(x):
    return abs(x)**(2/3)

def f8c(x):
    return abs(x)**(4/3)



################################################
####  MATH FUNCTIONS'S FIRST DERIVATIVES    ####
################################################


def df0(x):
    return 2

def df1(x):
    return 3*(x**2) - 3

def df2a(x):
    return 2*x

def df2b(x):
    return 2*x

def df3(x):
    return -(math.sin(x)) - 1

def df4(x):
    return df1(x)

def df5(x):
    return 3*(x**2) - 2

def df6(x):
    return math.exp(x)/((1+math.exp(x))**2)

def df7(x):
    return math.cos(x) - 1

def df8a(x):
    return (x**(1/3))/(3*abs(x))

def df8b(x):
    return 2/(3 * (x**(1/3)))

def df8c(x):
    return 4/3 * (x**(1/3))