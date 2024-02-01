from main import *
from math_functions import *

##############################################
####       TESTING NEWTON METHOD          ####
##############################################



###############
## Problem 1 ##
###############
# print("\nProblem 1\n")



###############
## Problem 2 ##
###############
# print("\nProblem 2\n")



###############
## Problem 3 ##
###############
# print("\nProblem 3\n")



## CLASS PROBLEMS BELOW



###############
## Problem 4 ##
###############
print("\nProblem 4\n")
newton(f4, df4, -0.8) 
"""
Finds the root in [1,2], which is the root furthest from initial guess.
Method ignores the two roots that are closest to the initial guess
"""



###############
## Problem 5 ##
###############
print("\nProblem 5\n")
newton(f5, df5, 0)
"""
In this case our guesses change from 0 to 1 infinitely.
The method gets "trapped" and cannot proceed. 
"""



###############
## Problem 6 ##
###############
print("\nProblem 6\n")

# a
print("part a")
newton(f6, df6, -3)
"""
# Initial guess is too far from the central vertical portion of the curve.
# The slope is very flat, which makes the guesses to diverge further and further from the root.
# Eventually reaches math range error because the x values get too large.
# Approaching a horizontal asymptote because started too far away
"""

print("part b")
#b
newton(f6, df6, -2)
"""
Initial guess is closer to zero, so it converges.
"""



###############
## Problem 7 ##
###############
print("\nProblem 7\n")
#various guesses
newton(f7, df7, 1)
newton(f7, df7, 0.1)
newton(f7, df7, 0)
newton(f7, df7, 0.0000001)
newton(f7, df7, -6.75)
'''
all guesses seem to work
'''



###############
## Problem 8 ##
###############
print("\nProblem 8\n")

# a and b won't work, c will work (according to Autry)
newton(f8a, df8a, 1) 
'''
the second guess in part a is -2, which produces a complex number once plugged into the f'(x)
since f'(x) includes the term x**1/3. As such, the function cannot continue generating as it
is not designed to work with complex numbers.
'''

newton(f8b, df8b, 1)
'''
same issue here with complex numbers as above, since the second guess is -0.5
'''

newton(f8c, df8c, 1)
'''
this one works well because, unlike parts a and b, the curve here inverts and allows for the slopes 
to point to positive values throughout all guesses, never going beyond zero to the left and causing 
complex numbers to appear in calculations 
'''