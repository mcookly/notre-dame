#!usr/bin/env python
"""
Max Cook
ACMS 40730
Homework 5, Problem 9
"""

import numpy as np
from pandas import read_csv
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt 

global A # Making A global allows xn_prime to work

### Read csv
file_data = np.array(read_csv("ivp.txt", header= None))
# NOTE: Make sure to change filename to 'ivp.txt' before submission.
dim = len(file_data[0]) # == number of equations
A = file_data[:dim, :dim].copy()
# Copy A so that changes to A won't affect file_data
IC = file_data[dim,].copy()
t_range = file_data[dim+1,].copy()
t_step = abs(t_range[0] - t_range[1]) / 10001
# Output results
print(f"A: {A}\nInitial Conditions: {IC}\nTime Range: {t_range}")


def xn_prime(t, x):
	eqs = list()
	for i in range(len(x)):
		eq = sum([A[i,j]*x[j] for j in range(len(x))])
		eqs.append(eq)
	return eqs

### Solve IVPs
sol = solve_ivp(xn_prime, t_range, IC, \
	max_step= t_step, \
	vectorized= True)

### Plot
plt.style.use("seaborn")
for i in range(dim):
	plt.plot(sol.t, sol.y[i,:], label= rf"$x_{i+1}$")
plt.xlabel(r"$t$")
plt.ylabel(r"$x(t)$")
plt.title("Components of Solution to IVP")
plt.legend()
plt.show()