#!usr/bin/env python
"""
Max Cook
ACMS 40730
Homework 6, Problem 2
Based on course code
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate


def F(A, S):
	athens = 0.03*A + 0.02*S - 0.000006*A*S
	sparta = 0.01*S - 0.000002*A*S
	return np.array([athens, sparta])
    

# Execute
plot_trajectories = True

initial_conditions = [

x_min = 0
x_max = total_pop

y_min = 0
y_max = total_pop

t_max = 10

num_x_arrows = 20
num_y_arrows = 20

arrow_spacing_x = (x_max-x_min)/num_x_arrows
arrow_spacing_y = (y_max-y_min)/num_y_arrows

x_range = np.arange(x_min, x_max, arrow_spacing_x)
y_range = np.arange(y_min, y_max, arrow_spacing_y)

X, Y = np.meshgrid(x_range, y_range)
U, V = F(X, Y)


norms = np.sqrt(U**2 + V**2)



# These lines control for floating point error.
# Set anything below the tolerance to be interpreted as 0
fp_tol = 10**-8
U[abs(U) < fp_tol] = 0
V[abs(V) < fp_tol] = 0


U = np.divide(U, norms, out = U, where = (norms!= 0))
V = np.divide(V, norms, out = V, where = (norms!= 0))
	
plt.quiver(X, Y, U, V, units = 'xy', angles='xy')
	
if plot_trajectories:
	for ic in initial_conditions:
		soln = scipy.integrate.solve_ivp(lambda t, y: F(y[0], y[1]), 
											(0, t_max), np.array(ic), 
											max_step = 1.0/400)
		plt.plot(soln.y[0], soln.y[1], linewidth = 3)

plt.style.use("seaborn")
plt.xlabel(r"$A$")
plt.ylabel(r"$S$")
plt.title("Populations of Athens and Sparta")

plt.axis('equal')

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))

plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)

plt.show()