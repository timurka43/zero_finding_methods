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