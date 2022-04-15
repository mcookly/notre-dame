#!usr/bin/env python
"""
Max Cook
ACMS 40730
Homework 6, Problem 6
"""

import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import numpy as np


# ---------- Parameters
plt.style.use("seaborn")

ALPHA = 1
BETA = 0.1
DELTA = 0.1
OMEGA = 1
gammas = [0, 2, 4, 7, 11]

# Form: (x0, y0, tau0)
ic = np.array([10, 0, 0])
tmax = 600

# ---------- Functions

# System of ODEs
def F(t, v, *args):
	# Can't seem to make solve_ivp work unless I pass all variables
	# into the function in one parameter.
	x, y, tau = v[0], v[1], v[2]
	gamma = args[0]

	dxdt = y
	dydt = gamma*np.cos(OMEGA*tau) - DELTA*y - BETA*x - ALPHA*x**3
	dtaudt = 1

	return np.array([dxdt, dydt, dtaudt])


def set_plot_chars(gamma):
	plt.xlabel(r"Time $t$")
	plt.ylabel(r"$x(t)$")
	plt.title(f"$x(t)$ at $\gamma={gamma}$")


# ---------- Calculate

for i in range(5):
	soln = solve_ivp(F, (0, tmax), ic, args=[gammas[i]])
	plt.figure(i+1)
	plt.plot(soln.t, soln.y[0], label = f"$\gamma={gammas[i]}$")
	set_plot_chars(gammas[i])


# ----------- Plot

plt.show()