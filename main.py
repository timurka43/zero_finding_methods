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
#   within 100 iterations, returns the approximated
#   value of such x
def bisection(f, x0, x1):
    return bisection_helper(f, x0, x1, 1) 

#recursive helper funciton 
def bisection_helper(f, x0, x1, iter):
    print("Current Interval [", x0, ",", x1, "]" )
    midpoint = float(x0+x1)/2 # calculate midpoint 
    left = f(float(x0)) # calculate and store f(x) for the three values
    right =  f(float(x1))
    middle = f(midpoint)
    if (left * right >= 0):
        raise ValueError("The initial guess points must produce opposite signs when plugged into the function")
    #base case: found midpoint on x-axis or performed 100 iterations
    if (middle < 0.00001 and middle > -0.00001) or (iter >= 100): #termination conditions: 100 iterations or found zero within 0.00001 uncertainty
        print ("Iterations:", iter)
        print("Zero at x=", midpoint)
        return midpoint
    #recursive cases
    elif (left*middle < 0): # if zero is in the left half
        iter += 1
        return bisection_helper(f, x0, midpoint, iter) # recurse on the left half
    elif (middle*right < 0): # if zero is in the right half
        iter += 1
        return bisection_helper(f, midpoint, x1, iter) # recurse on the right half
    


## NEWTON'S METHOD ##
    
def newton(f, f_prime, x0):
    return newton_helper(f, f_prime, x0, 1)

def newton_helper(f, f_prime, x0, iter):
    print("Current guess: ", x0)
    #find the value of f(x0)
    value = f(float(x0))
    print("Value:", value)
    # print("f(x)=", value)
    #if found zero, terminate
    if (value == 0):
        print ("Iterations:", iter)
        print("Zero at x=", x0, "\n")
        return x0
    #find the value of f'(x0)
    slope = f_prime(float(x0))
    print("Slope:", slope)
    # print("f'(x)=", slope)
    #check that the slope is not zero
    if (slope == 0):
        raise ValueError("Slope is zero, cannot find the next guess.\nChoose a different initial guess")
    #find the new guess for x s.t. f(x1)=0
    x1 = x0 - float(value/slope)
    #if the new guess produces zero or it's not different from prev. guess, or MAXITER iterations, terminate
    if (f(x1) == 0) or (abs(x1-x0) < TOLERANCE) or (iter >= MAXITER):
        print ("Iterations:", iter)
        print("Zero at x≈", x1, "\n")
        return x1
    else:
        iter += 1
        return newton_helper(f, f_prime, x1, iter)
    



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
