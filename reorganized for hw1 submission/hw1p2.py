"""
Title: Homework 1, part 2. Pathological Cases
Author: Timur Kasimov (Grinnell, 2025)
Data Created: February, 2024
Date Updated: February 12, 2024

Purpose: Implement Newton's method and test pathological cases.

This is a homework assignment for my Computational Methods Class
"""

import math

MAXITER = 1000
TOLERANCE = 1e-10

#####################
## NEWTON'S METHOD ##
#####################
def newton(f, df, x0):
    for i in range(1, MAXITER+1):
        # print("Current guess: ", x0)
        #find the value of f(x0) 
        value = f(float(x0))
        if (value == "overflow"):
            print("OVERFLOW, cannot find zero\n")
            return "overflow"
        # print("f(x)=", value) # debugging
        #if found zero, terminate
        if (value == 0):
            print ("Iterations:", i)
            print("Zero at x=", round(x0, 6), "\n")
            return round(x0, 6)
        #find the value of f'(x0)
        slope = df(float(x0))
        # print("f'(x)=", slope) # debugging
        #check that the slope is not zero
        if (type(slope) == complex):
            print("COMPLEX NUMBER\n")
            return "COMPLEX NUMBER"
        if (slope == 0):
            raise ValueError("Slope is zero, cannot find the next guess.\nChoose a different initial guess")
        #find the new guess for x s.t. f(x1) is closer to 0
        x1 = x0 - float(value/slope)
        #if the new guess is not different from prev guess (within tolerance) , then terminate
        if (abs(x1-x0) < TOLERANCE):
            print ("Iterations:", i)
            print("Zero at x≈", round(x1, 6))
            return round(x1, 6)
        else:
            # update the current guess, iterate again
            x0 = x1
    print("REACHED MAXIMUM NUMBER OF ITERATIONS")
    print("The closest approximation of zero is at x=", round(x0, 6))
    return round(x0, 6)



################################
####     MATH FUNCTIONS     ####
################################

def f4(x):
    return x**3 - 3*x + 1

def f5(x):
    return x**3 - 2*x + 2

def f6(x):
    if (x>299999):
        print("Overflow for math.exp() function")
        return "overflow"
    else:
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

def df4(x):
    return 3*(x**2) - 3

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




##############################################
##############################################
####       TESTING NEWTON METHOD          ####
##############################################
##############################################

if __name__ == "__main__":

    ###############
    ## Problem 1 ##
    ###############
    print("\n\nProblem 1\n")
    newton(f4, df4, -0.8) 
    """
    Finds the root in [1,2], which is the root furthest from initial guess.
    Method ignores the two roots that are closest to the initial guess.
    While this is not "ideal" behavior of the Newton's function, it is 
    understandable based of how it draws a tangent line using the first
    derivative and then uses that tangent line to approximate zero and 
    provide the next guess. This next guess ends up being closer to the 
    zero in the interval [1,2] and eventually finds it.
    """



    ###############
    ## Problem 2 ##
    ###############
    print("\n\nProblem 2\n")
    newton(f5, df5, 0)
    """
    In this case our guesses change from 0 to 1 infinitely.
    The method gets "trapped" and simply reaches the maximum number 
    of iterations.
    """



    ###############
    ## Problem 3 ##
    ###############
    print("\n\nProblem 3\n")

    # a
    print("part a")
    newton(f6, df6, -3)
    """
    Initial guess is too far from the central vertical portion of the curve.
    The slope is very flat, which makes the guesses to diverge further and further from the root.
    Eventually reaches math range error because the x values get too large.
    Approaching a horizontal asymptote because started too far away.

    I decided to include a helpful message as an output instead of having 
    the method throw an error at you.
    """

    print("part b")
    #b
    newton(f6, df6, -2)
    """
    Initial guess is closer to zero, so it converges.
    """



    ###############
    ## Problem 4 ##
    ###############
    print("\n\nProblem 4\n")
    #various guesses
    newton(f7, df7, 1)
    newton(f7, df7, 0.1)
    newton(f7, df7, 0)
    newton(f7, df7, 0.0000001)
    newton(f7, df7, -6.75)
    '''
    All guesses seem to work.

    I implemented the Newton's method to always check the
    value of the function at the guess before calculating the value
    of the derivative function. Thus, even when the slope is zero,
    we do not get to the error message because that is also when 
    the value of the function is zero. 

    Plotting the function, we see that there are cases when the value 
    of the derivative is zero, but the value of the funciton is not zero. 
    Thus, if we were to come across such a point with our value of the derivative, 
    the method would throw an error at us. However, neither of the cases above 
    cause this to happen.
    '''



    ###############
    ## Problem 5 ##
    ###############
    print("\n\nProblem 5\n")

    # a and b won't work, c will work (according to Autry)
    newton(f8a, df8a, 1) 
    '''
    the second guess in part a is -2, which produces a complex number once plugged into the f'(x)
    since f'(x) includes the term x**1/3. As such, the function cannot continue generating as it
    is not designed to work with complex numbers.

    I implemented the Newton's method so it provides a helpful message without
    throwing an error.
    '''

    newton(f8b, df8b, 1)
    '''
    Same issue here with complex numbers as above, since the second guess is -0.5
    '''

    newton(f8c, df8c, 1)
    '''
    This one works well because, unlike parts a and b, the curve here inverts and allows for the slopes 
    to point to positive values throughout all guesses, never going beyond zero to the left and never causing 
    complex numbers to appear in calculations 
    '''