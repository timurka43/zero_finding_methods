from main import *

##############################################
####       TESTING NEWTON METHOD          ####
##############################################


# ## Problem 1 ##
# print("\nProblem 1\n")

# ## Problem 2 ##
# print("\nProblem 2\n")


# ## Problem 3 ##
# print("\nProblem 3\n")





## CLASS PROBLEMS BELOW



# ## Problem 4 ## 
# print("\nProblem 4\n")
# newton(f4, df4, -0.8) 
# """
# finds the root in [1,2], which is the root furthest from initial guess
# method ignores the two roots that are closest to the initial guess
# """


# ## Problem 5 ##
# print("\nProblem 5\n")
# newton(f5, df5, 0)
# """
# in this case our guesses changes from 0 to 1 infinitely
# the method gets "trapped" and cannot proceed. 
# """



# ## Problem 6 ##
# print("\nProblem 6\n")

# # a
# newton(f6, df6, -3)
# """
# # Initial guess is too far from the central vertical portion of the curve
# # slope is very flat, which makes the guesses to diverge further and further from the root, 
# # eventually reaches math range error because the x values get too large.
# # Approaching a horizontal asymptote because started too far away
# """
# #b
# newton(f6, df6, -2)
# """
# Initial guess is closer to zero, so it converges.
# """




# ## Problem 7 ##
# print("\nProblem 7\n")
# #various guesses
# newton(f7, df7, 1)
# newton(f7, df7, 0.1)
# newton(f7, df7, 0)
# newton(f7, df7, 0.0000001)
# newton(f7, df7, -6.75)

# '''
# all guesses seem to work
# '''


## Problem 8 ##
print("\nProblem 8\n")

# a and b won't work, c will work (according to Autry)
newton(f8a, df8a, 1)
# newton(f8b, df8b, 1)
# newton(f8c, df8c, 1)





