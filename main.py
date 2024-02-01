"""
Title: Zero Finding Methods
Author: Timur Kasimov (Grinnell, 2025)
Data Created: January 29, 2024
Date Updated: January 30, 2024

Purpose: Implement and test 3 zero finding methods: Bisection, Newton's, and Secant methods.

This is a homework assignment for my Computational Methods Class
"""

##  REWRITE ALL FUNCTIONS ITERATIVELY INSTEAD OF RECURSIVELY

# import numpy
# import scipy
import math

MAXITER = 1000
TOLERANCE = 1e-10


#####################################
####    ZERO-FINDING METHODS     ####
#####################################


## BISECTION METHOD ##

# pre-conditions: 
#   f - mathematical function f(x)
#   x0, x1 - initial guess points for f(x) = 0
# post-conditions:
#   returns the real number x s.t. f(x) ≈ 0 or 
#   in the case that such x was not found 
#   within MAXITER iterations, returns the approximated
#   value of such x
def bisection(f, x0, x1):
    ## run the loop iteratively at most MAXITER times
    for i in range(1, MAXITER+1):
        # print("Current Interval [", x0, ",", x1, "]" )
        x_mid = float(x0+x1)/2 # calculate midpoint 
        left = f(float(x0)) # calculate and store f(x) for the three values
        right =  f(float(x1))
        middle = f(x_mid)
        if (left * right >= 0):
            raise ValueError("The initial guess points must produce opposite signs when plugged into the function")
        #termination condition: found midpoint that produced zero in the variable middle
        if (abs(middle) < TOLERANCE):
            print ("Iterations:", i)
            print("Zero at x=", round(x_mid, 10))
            return round(x_mid, 10)
        #updating boundaries
        elif (left*middle < 0): # if zero is in the left half
            x1 = x_mid # causes iteration on the left half
        elif (middle*right < 0): # if zero is in the right half
            x0 = x_mid # causes iteration on the right half
    print("REACHED MAXIMUM NUMBER OF ITERATIONS")
    print("The closest approximation of zero is at x=", round(x_mid, 10))
    return round(x_mid, 10)
    


## NEWTON'S METHOD ##
    
def newton(f, df, x0):
    return newton_helper(f, df, x0, 1)

def newton_helper(f, df, x0, iter):
    for i in range(1, MAXITER+1):
        print("Current guess: ", x0)
        #find the value of f(x0)
        value = f(float(x0))
        # print("f(x)=", value)
        #if found zero, terminate
        if (value == 0):
            print ("Iterations:", i)
            print("Zero at x=", round(x0, 10), "\n")
            return x0
        #find the value of f'(x0)
        slope = df(float(x0))
        # print("f'(x)=", slope)
        #check that the slope is not zero
        if (slope == 0):
            raise ValueError("Slope is zero, cannot find the next guess.\nChoose a different initial guess")
        #find the new guess for x s.t. f(x1) is closer to 0
        x1 = x0 - float(value/slope)
        #if the new guess is not different from prev guess (within tolerance) , then terminate
        if (abs(x1-x0) < TOLERANCE):
            print ("Iterations:", i)
            print("Zero at x≈", round(x1, 10), "\n")
            return round(x1, 10)
        else:
            # update the current guess, iterate again
            x0 = x1
    print("REACHED MAXIMUM NUMBER OF ITERATIONS")
    print("The closest approximation of zero is at x=", round(x0, 10))
    return round(x0, 10)
    



## SECANT METHOD ##

def secant(f, x0, x1):
        return secant_helper(f, x0, x1, 1)
    
def secant_helper(f, x0, x1, iter):
    print("Current guesses: [", x0, ",", x1, "]")
    #find the values of f(x0) and f(x1)
    value0 = f(float(x0))
    value1 = f(float(x1))
    # calculate the new guess for zero, x2
    x2 = x1 - value1 * (x1-x0) / (value1 - value0)
    # # check if found zero within small uncertainty or 
    # or if the absolute difference between x2 and x1 is small/negligible
    # or ran 100 iterations
    value2 = f(float(x2))
    if (abs(value2) < 0.000001) or (abs(x2-x1) < 0.000001) or  (iter >= 100):
        print ("Iterations:", iter)
        print("Zero at x≈", x2)
        return x2
    else:
        iter += 1
        return secant_helper(f, x1, x2, iter)
