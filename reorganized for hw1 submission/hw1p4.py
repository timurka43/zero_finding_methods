"""
Title: Homework 1, part 4. Error convergence
Author: Timur Kasimov (Grinnell, 2025)
Data Created: February 13, 2024
Date Updated: February 13, 2024

Purpose: Implement and test 3 zero finding methods: Bisection, Newton's, and Secant methods.

This is a homework assignment for my Computational Methods Class
"""

import math
import matplotlib.pyplot as plt

MAXITER = 1000
TOLERANCE = 1e-10

#############################################
#############################################
####    ZERO-FINDING METHODS,            ####
####    RETURNING LIST OF ALL GUESSES    ####
#############################################
#############################################

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
    guesses = [x0, x1]
    ## run the loop iteratively at most MAXITER times
    for i in range(1, MAXITER+1):
        # print("Current Interval [", x0, ",", x1, "]" )
        x_mid = float(x0+x1)/2 # calculate midpoint 
        left = f(float(x0)) # calculate and store f(x) for the three values
        right =  f(float(x1))
        middle = f(x_mid)
        guesses.append(x_mid)
        if (left * right >= 0):
            raise ValueError("The initial guess points must produce opposite signs when plugged into the function")
        #termination condition: found midpoint that produced zero in the variable middle
        if (abs(middle) < TOLERANCE):
            print ("Iterations:", i)
            print("Zero at x=", round(x_mid, 6))
            return guesses
        #updating boundaries
        elif (left*middle < 0): # if zero is in the left half
            x1 = x_mid # causes iteration on the left half
        elif (middle*right < 0): # if zero is in the right half
            x0 = x_mid # causes iteration on the right half
    print("REACHED MAXIMUM NUMBER OF ITERATIONS")
    print("The closest approximation of zero is at x=", round(x_mid, 6))
    return guesses
    

#####################
## NEWTON'S METHOD ##
#####################
def newton(f, df, x0):
    guesses = [x0]
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
            return guesses
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
        guesses.append(x1)
        #if the new guess is not different from prev guess (within tolerance) , then terminate
        if (abs(x1-x0) < TOLERANCE):
            print ("Iterations:", i)
            print("Zero at x≈", round(x1, 6))
            return guesses
        else:
            # update the current guess, iterate again
            x0 = x1
    print("REACHED MAXIMUM NUMBER OF ITERATIONS")
    print("The closest approximation of zero is at x=", round(x0, 6))
    return guesses
    


###################
## SECANT METHOD ##
###################
def secant(f, x0, x1):
    guesses = [x0, x1]
    for i in range(1, MAXITER+1):
        # print("Current guesses: [", x0, ",", x1, "]")
        #find the values of f(x0) and f(x1)
        value0 = f(float(x0))
        value1 = f(float(x1))
        # calculate the new guess for zero, x2
        x2 = x1 - value1 * (x1-x0) / (value1 - value0)
        guesses.append(x2)
        value2 = f(float(x2))
        # # check if found zero within small uncertainty or 
        # or if the absolute difference between x2 and x1 is small/negligible
        if (abs(value2) < TOLERANCE) or (abs(x2-x1) < TOLERANCE):
            print ("Iterations:", i)
            print("Zero at x≈", round(x2, 6))
            return guesses
        else:
             # update guesses 
            x0 = x1 
            x1 = x2
    print("REACHED MAXIMUM NUMBER OF ITERATIONS")
    print("The closest approximation of zero is at x=", round(x0, 6), "\n")
    return guesses





################################
####     MATH FUNCTIONS     ####
################################

def f1(x):
    return (x-1)*(x-2)*(x-3)

def f2(x):
    return (x-1)**3


################################################
####  MATH FUNCTIONS'S FIRST DERIVATIVES    ####
################################################

def df1(x):
    return 3*x*x - 12*x + 11

def df2(x):
    return 3*((x-1)**2)


#########################################
####     FUNCTION TO PLOT ERRORS     ####
#########################################
def plot_errors(guesses, x_bar, title):
    errors = []
    for val in guesses:
        errors.append(abs(x_bar - val))
    # plotting all but the last errors on x-axis, and all but the first errors on y-axis
    plt.loglog(errors[:-1], errors[1:])
    plt.title(title)
    plt.show()


if __name__ == "__main__":

    #####################
    ###   PROBLEM 1   ###
    ##################### 

    print("\nProblem 1\n")

    print("\nBisection")
    guesses_bisection = bisection(f1, 0, 1.5)
    plot_errors(guesses_bisection, 1, "Problem 1, Bisection")
    ''' the slope of the line appears to be 1'''


    print("\nNewton")
    gusses_newton = newton(f1, df1, 0.1)
    plot_errors(gusses_newton, 1, "Problem 1, Newton")
    ''' the slope of the line appears to be 2'''
    

    print("\nSecant")
    guesses_secant = secant(f1, 1.1, 1.2)
    plot_errors(guesses_secant, 1, "Problem 1, Secant")
    ''' the slope of the line appears to be 1.6'''



    #####################
    ###   PROBLEM 2   ###
    ##################### 

    print("\n\n\nProblem 2")

    print("\nBisection")
    guesses_bisection = bisection(f2, 0, 1.5)
    plot_errors(guesses_bisection, 1, "Problem 2, Bisection")
    ''' the slope of the line appears to be 1'''


    print("\nNewton")
    gusses_newton = newton(f2, df2, 0.1)
    plot_errors(gusses_newton, 1, "Problem 2, Newton")
    ''' the slope of the line appears to be 1, not 2 like previously'''
    

    print("\nSecant")
    guesses_secant = secant(f2, 1.1, 1.2)
    plot_errors(guesses_secant, 1, "Problem 2, Secant")
    ''' the slope of the line appears to have decreased to 1 also? Not sure.'''
    