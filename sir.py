# sir.py
# Eric A. Autry
# CSC 395 Spring 2024
# 02/01/24

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

"""
sirFunc: this function computes the RHS of the ODE for use in the solver.

y: the current solution vector
t: the current time
R0: the basic reproductive number, from the model

dydt: the RHS of the ODE
"""
def sirFunc(y, t, R0):
	ss, ii, rr = y
	dydt = [-R0*ss*ii, R0*ss*ii-ii, ii]
	return dydt


"""
sir: this function will solve the ODE using scipy's built in solver, and 
     returns the solution S,I,R at the time T given the initial vector and R0.

initVec: the initial values of S,I,R at time t=0
T: the final time to solve until
R0: the basic reproductive number, from the model

Returns the values S(T),I(T),R(T).
"""
def sir(initVec, T, R0):
	tt = [0, T]
	sol = odeint(sirFunc, initVec, tt, args=(R0,))
	return (sol[-1][0], sol[-1][1], sol[-1][2])


"""
sirForPlot: this solve the ODE over a time interval to give the solution for 
            use in plotting.

initVec: the initial values of S,I,R at time t=0
T: the final time to solve until
N: the number of intermediate points to use for plotting
R0: the basic reproductive number, from the model

sol: the matrix representing the solution
tt: the vector of timesteps used, corresponding to the matrix sol
"""
def sirForPlot(initVec, T, N, R0):
	tt = np.linspace(0, T, N)
	sol = odeint(sirFunc, initVec, tt, args=(R0,))
	return sol, tt

"""
plotSIR: will generate a plot of the SIR solution for the given inputs.

initVec: the initial values of S,I,R at time t=0
T: the final time to solve until
N: the number of intermediate points to use for plotting
R0: the basic reproductive number, from the model

Creates and displays a corresponding plot, no return value.
"""
def plotSIR(initVec, T, N, R0):
	sol, tt = sirForPlot(initVec, T, N, R0)
	plt.plot(tt, sol[:,0], 'b', label='S')
	plt.plot(tt, sol[:,1], 'r', label='I')
	plt.plot(tt, sol[:,2], 'g', label='R')
	plt.legend(loc='best')
	plt.xlabel('t')
	plt.grid()
	plt.show()
	return

"""
Python's "main function" block.
"""
if __name__ == "__main__":

	# Example scenario with initial infection of 1% of population and R0=5.
	# Solving until time T=4, with 1000 intermediate steps for plotting.
	init = [.99, 0.01, 0]
	T = 4
	R0 = 5
	N = 1000

	# Get the values at time T=4.
	sFin, iFin, rFin = sir(init, T, R0)
	print("T=4, R0=5, I0=0.01")
	print(sFin, iFin, rFin)
	print()

	# Get the values at time T=1.5.
	sFin, iFin, rFin = sir(init, 1.5, R0)
	print("T=1.5, R0=5, I0=0.01")
	print(sFin, iFin, rFin)

	# Plot the solution through time T=4.
	plotSIR(init, T, N, R0)