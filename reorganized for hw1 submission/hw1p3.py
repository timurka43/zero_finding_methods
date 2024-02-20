"""
Title: Homework 1, part 3. SIR Model
Author: Timur Kasimov (Grinnell, 2025)
Data Created: February, 2024
Date Updated: February 13, 2024

Purpose: Estimate the peak of the I (infectious) curve in the SIR Model

This is a homework assignment for my Computational Methods Class
"""
import math
from sir import *
import matplotlib.pyplot as plt

MAXITER = 1000
TOLERANCE = 1e-10


'''
In order to find the maximum of the curve I, we need to find where its first 
derivative is zero.
Need to define the two functions you will feed to your newton method
'''


def dIdt(init, t, R0):  
    ##need to calculate S(t) and I(t) first
    St, It, Rt = sir(init, t, R0)
    ## then use formula for dIdt: R0SI - I
    return R0*St*It - It

    

def d2Idt2(init, t, R0):
    ##need to calculate S(t) and I(t) first
    St, It, Rt = sir(init, t, R0)
    ## then use formula for d2Idt2:
    return -(R0*R0)*St*(It*It) + ((R0*St-1)**2)*It

'''
Rewrite Newton's method now so it takes in init vector and R0 as parameters.
The new method does not need to take f(x) and df(x) since these functions are
predefined for the netwon approach to sir simulation specifically. Just have newton_sir
use these two functions without having to take them in as parameters.

Instead, the method takes the initialized vector with S, I, R values,
R0 constant, and the initial guess t (guessed time of the peak).
'''
def newton_sir(init, t, R0):
    guesses = [t]
    for i in range(1, MAXITER+1):
        # print("Current guess: ", x0)
        #find the value of f(x0) 
        value = dIdt(init, float(t), R0)
        if (value == "overflow"):
            print("OVERFLOW, cannot find zero\n")
            return "overflow"
        # print("f(x)=", value) # debugging
        #if found zero, terminate
        if (value == 0):
            print ("Iterations:", i)
            print("Zero at x=", round(t, 6), "\n")
            return guesses
        #find the value of f'(x0)
        slope = d2Idt2(init, float(t), R0)
        # print("f'(x)=", slope) # debugging
        #check that the slope is not zero
        if (type(slope) == complex):
            print("COMPLEX NUMBER\n")
            return "COMPLEX NUMBER"
        if (slope == 0):
            raise ValueError("Slope is zero, cannot find the next guess.\nChoose a different initial guess")
        #find the new guess for x s.t. f(x1) is closer to 0
        t1 = t - float(value/slope)
        guesses.append(t1)
        #if the new guess is not different from prev guess (within tolerance) , then terminate
        if (abs(t1-t) < TOLERANCE):
            print ("Iterations:", i)
            print("Zero at x≈", round(t1, 6), "\n")
            return guesses
        else:
            # update the current guess, iterate again
            t = t1
    print("REACHED MAXIMUM NUMBER OF ITERATIONS")
    print("The closest approximation of zero is at x=", round(t, 6), "\n")
    return guesses




#########################################
####     FUNCTION TO PLOT ERRORS     ####
#########################################
def plot_errors(guesses, title):
    errors = []
    ## record length to access the last element/guess later
    length = len(guesses)
    ## calculate errors using the last guess as x-bar
    for val in guesses:
        errors.append(abs(guesses[length-1] - val))
    # plotting all but the last errors on x-axis, and all but the first errors on y-axis
    plt.loglog(errors[:-1], errors[1:])
    plt.title(title)
    plt.show()




##################
### MAIN BLOCK ###
##################
if __name__ == "__main__":

    ##############
    # Scenario 1 #
    ##############
    print("\n\nScenario 1\n")
    init_vec = [0.99, 0.01, 0.00]
    R0 = 5

    # trial 1 
    guesses_1 = newton_sir(init_vec, 1.5, R0)
    plot_errors(guesses_1, "Newton SIR, Scenario 1, Trial 1")
    '''The slope appears to be 2.'''

    # trial 2
    newton_sir(init_vec, 2, R0)

    # trial 3
    newton_sir(init_vec, 1.869697 , R0)



    ##############
    # Scenario 2 #
    ##############
    print("\n\nScenario 2\n")
    init_vec = [0.999, 0.001, 0.00]
    R0 = 2

    # trial 1 
    guesses_2 = newton_sir(init_vec, 6.5, R0)
    plot_errors(guesses_2, "Newton SIR, Scenraio 2, Trial 1")
    '''The slope appears to be 2 again.'''

    # trial 2
    newton_sir(init_vec, 5, R0)

    # trial 3
    newton_sir(init_vec, 7 , R0)



    ##############
    # Scenario 3 #
    ##############
    print("\n\nScenario 3\n")
    init_vec = [0.999, 0.001, 0.00]
    R0 = 4

    # trial 1 
    guesses_3 = newton_sir(init_vec, 2.5, R0)
    plot_errors(guesses_3, "Newton SIR, Scenario 3, Trial 1")
    '''The slope appears to be less than 2 in this case.'''