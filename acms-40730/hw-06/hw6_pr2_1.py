#!usr/bin/env python
"""
Max Cook
ACMS 40730
Homework 6, Problem 2
"""

from turtle import width
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

# System of ODEs
def F(A, S):
	aprime = 0.03*A + 0.02*S - 0.000006*A*S
	sprime = 0.01*S - 0.000002*A*S
	return np.array([aprime, sprime])


# Parameters
nmin = 0
nmax = 20000
nstep = 1000
tmax = 50

a = np.linspace(nmin, nmax, nstep)
s = a
av, sv = np.meshgrid(a, s)

# (A0, S0)
ics = list()
ic_step = 2000
icx = list(range(nmin, nmax, ic_step))
icy = icx

for x0 in icx:
	for y0 in icy:
		ics.append((x0, y0))


# Calculate
plt.style.use("seaborn") # Use before plotting the ICs

aprime, sprime = F(av, sv)
# for ic in ics:
# 	soln = solve_ivp(lambda t, y: F(y[0], y[1]), (0, tmax), np.array(ic))
# 	plt.plot(soln.y[0], soln.y[1], linewidth = 2)


# Plot
plt.streamplot(av, sv, aprime, sprime, \
	color = "lightslategray", \
	linewidth = .75, \
	density = 2)

plt.xlim(nmin, nmax)
plt.ylim(nmin, nmax)
plt.xlabel("A")
plt.ylabel("S")
plt.show()