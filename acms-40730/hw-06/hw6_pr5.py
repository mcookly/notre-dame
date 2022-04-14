#!usr/bin/env python
"""
Max Cook
ACMS 40730
Homework 6, Problem 5
"""

import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import numpy as np


# ---------- Parameters
plt.style.use("seaborn")

tmax = 10
ics = [(1,2), (5,1), (0.5,5), (3,5), (1,3.5), (6,4), (4,8)]

# For vector field
points = np.linspace(0, tmax, 31)
xp, yp = np.meshgrid(points, points)


# ---------- Functions

# System of ODEs
def F(x, y):
	dxdt = 1 + pow(x,2)*y - 4*x
	dydt = 3*x - pow(x,2)*y

	return np.array([dxdt, dydt])


# ---------- Calculate

### Vector field
xv, yv = F(xp, yp)

## Normalize vector field
# Found this elegant solution here:
# https://stackoverflow.com/questions/17769341/dealing-with-zeros-in-numpy-array-normalization

# Avoid vectors that are zero
norms = norm = np.sqrt(xv**2 + yv**2)
nonzero_norms = norms > 0
# Normalize
xv[nonzero_norms] /= norms[nonzero_norms]
yv[nonzero_norms] /= norms[nonzero_norms]

# Plot vector field
plt.figure(1) # Second figure is for solutions v. time
plt.quiver(xp, yp, xv, yv, color = "lightslategray", \
	units = "xy", angles = "xy")

### Solve IVP using initial conditions

for ic in ics:
	soln = solve_ivp(lambda t,y: F(y[0], y[1]), (0, tmax), np.array(ic), \
		max_step = 0.05)
	plt.figure(1)
	plt.plot(soln.y[0], soln.y[1])
	
	if ic == (1, 2):
		plt.figure(2)
	elif ic == (5,1):
		plt.figure(3)
	else:
		continue
	
	plt.plot(soln.t, soln.y[0], label = r"$x(t)$")
	plt.plot(soln.t, soln.y[1], label = r"$y(t)$")


# ----------- Plot properties

## ODE system
plt.figure(1)
plt.axis("square")
plt.xlim((0, tmax))
plt.ylim((0, tmax))
plt.xlabel(r"$\frac{dx}{dt}$")
plt.ylabel(r"$\frac{dy}{dt}$")
plt.title("Phase Plane of ODEs")

## Solutions v. time

for i in range(2):
	plt.figure(i+2)
	plt.xlabel("Time $t$")
	plt.ylabel("Chemical")
	plt.title(f"Chemical Reaction v. Time for {ics[i]}")
	plt.legend()

plt.show()