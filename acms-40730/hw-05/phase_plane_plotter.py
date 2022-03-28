#!usr/bin/env python
"""
Max Cook
ACMS 40730
Homework 5, Problems 5-7
"""

# from math import exp
from logging import logMultiprocessing
from turtle import color
from matplotlib import units
import numpy as np
import matplotlib.pyplot as plt

### Equations
def eq5(x, y):
	# Return: [x', y']
	xprime = -x + 4*y
	yprime = 2*x + y
	return xprime, yprime

def plt_phase_plane():
	pass


# Parameters
rad = 30 # radius of viewing window
nsteps = 20

# Calculate
xv, yv = np.meshgrid(np.linspace(-rad, rad, nsteps), np.linspace(-rad, rad, nsteps))
xprime, yprime = eq5(xv, yv)


# Plot
plt.style.use("seaborn")
# plt.quiver(xv, yv, xprime, yprime, \
# units = "xy", \
# angles = "xy", \
# scale_units = "xy", \
# scale = 20, \
# width = .2, \
# color = "slategray")

# Plot direction field
plt.streamplot(xv, yv, xprime, yprime, color= "slategray", \
	density= 2, linewidth= 1)

# Plot solutions

plt.axis("square")
plt.show()