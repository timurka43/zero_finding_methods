"""
Title: Homework 1, part 1. Zero Finding Methods
Author: Timur Kasimov (Grinnell, 2025)
Data Created: January 29, 2024
Date Updated: February 12, 2024

Purpose: Implement and test 3 zero finding methods: Bisection, Newton's, and Secant methods.

This is a homework assignment for my Computational Methods Class
"""

import math

MAXITER = 1000
TOLERANCE = 1e-10

#####################################
#####################################
####    ZERO-FINDING METHODS     ####
#####################################
#####################################

######################
## BISECTION METHOD ##
######################
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
            print("Zero at x=", round(x_mid, 6))
            return round(x_mid, 6)
        #updating boundaries
        elif (left*middle < 0): # if zero is in the left half
            x1 = x_mid # causes iteration on the left half
        elif (middle*right < 0): # if zero is in the right half
            x0 = x_mid # causes iteration on the right half
    print("REACHED MAXIMUM NUMBER OF ITERATIONS")
    print("The closest approximation of zero is at x=", round(x_mid, 6))
    return round(x_mid, 6)
    

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
    


###################
## SECANT METHOD ##
###################
def secant(f, x0, x1):
    for i in range(1, MAXITER+1):
        # print("Current guesses: [", x0, ",", x1, "]")
        #find the values of f(x0) and f(x1)
        value0 = f(float(x0))
        value1 = f(float(x1))
        # calculate the new guess for zero, x2
        x2 = x1 - value1 * (x1-x0) / (value1 - value0)
        value2 = f(float(x2))
        # # check if found zero within small uncertainty or 
        # or if the absolute difference between x2 and x1 is small/negligible
        if (abs(value2) < TOLERANCE) or (abs(x2-x1) < TOLERANCE):
            print ("Iterations:", i)
            print("Zero at x≈", round(x2, 6))
            return round(x2, 6)
        else:
             # update guesses 
            x0 = x1 
            x1 = x2
    print("REACHED MAXIMUM NUMBER OF ITERATIONS")
    print("The closest approximation of zero is at x=", round(x0, 6), "\n")
    return round(x0, 6)




################################
####     MATH FUNCTIONS     ####
################################

def f1(x):
    return x**3 - 3*x + 1

def f2a(x):
    return x**2 - 2

def f2b(x):
    return x**2 - 3

def f3(x):
    return math.cos(x) - x



################################################
####  MATH FUNCTIONS'S FIRST DERIVATIVES    ####
################################################

def df1(x):
    return 3*(x**2) - 3

def df2a(x):
    return 2*x

def df2b(x):
    return 2*x

def df3(x):
    return -(math.sin(x)) - 1



###################
###################
##    TESTING    ##
###################
###################

if __name__ == "__main__":

    ###############
    ## Problem 1 ##
    ###############
    print("\nProblem 1 (a)")
    
    # part A

    #Bisection
    print("\nBisection: (a)")
    bisection(f1, 1, 2)
        
    #Newton
    print("\nNewton (a)")
    newton(f1, df1, 2)
    
    #Secant
    print("\nSecant (a)")
    secant(f1, 1, 2)


    # part B
    print("\nProblem 1 (b)")

    #Bisection
    print("\nBisection (b)")
    bisection(f1, 0, 1)

    #Newton
    print("\nNewton (b)")
    newton(f1, df1, 0)

    #Secant
    print("\nSecant (b)")
    secant(f1, 0, 1)



    ###############
    ## Problem 2 ##
    ###############

    #part A

    print("\n\n\n\nProblem 2 (a)")
        
    #Bisection
    print("\nBisection (a)\n")
    bisection(f2a, 0, 2)
        
    #Newton
    print("\nNewton (a)\n")
    newton(f2a, df2a, 1)

    #Secant
    print("\nSecant (a)\n")
    secant(f2a, 1, 2)


    # part B

    print("\n\nProblem 2 (b)")
        
    #Bisection
    print("\nBisection (b)\n")
    bisection(f2b, 0, 2)
        
    #Newton
    print("\nNewton (b)\n")
    newton(f2b, df2b, 1)
    
    #Secant
    print("\nSecant (b)\n")
    secant(f2b, 0, 2)



    ###############
    ## Problem 3 ##
    ###############
    print("\n\n\n\nProblem 3\n")
        
    #Bisection
    print("\nBisection\n")
    bisection(f3, 0, 1)
        
    #Newton
    print("\nNewton\n")
    newton(f3, df3, 0)
    
    #Secant
    print("\nSecant\n")
    secant(f3, 0, 1)