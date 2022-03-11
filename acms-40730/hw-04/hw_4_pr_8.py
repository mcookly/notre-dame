#!usr/bin/env python
"""
Max Cook
ACMS 40730
Homework 4, Problem 8
"""

from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import numpy as np


# ODE
def x_prime(t, x):
	return x - 2*t*pow(x,2)


# Input
INIT_COND = float(input("Please enter an initial condition: "))

# Calculate
solved = solve_ivp(x_prime, (0.0, 10.0), [INIT_COND,])

# Display
plt.style.use("seaborn")
plt.plot(solved.t, solved.y[0])
plt.show()