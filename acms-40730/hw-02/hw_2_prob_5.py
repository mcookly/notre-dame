#!usr/bin/env python
"""
Max Cook
ACMS 40730
Homework 2, Problem 5
"""

"""
Algorithm:
- The species reproduces in discrete generations.
- At each generation, alpha_m portion of the male members die, and alpha_f portion of the female
members die.
- At each generation, each female member (who was alive during the previous generation)
produces k_m male offspring and k_f female offspring.
- The initial population of males is m0 and the initial population of females is f0.
"""

import matplotlib.pyplot as plt
import numpy as np


# (b) Parameters
n = 11 # to include n = 10
n_range = range(n)
a_m, a_f = 0.25, 0.2
k_m, k_f = 0.54, 0.50
m, f = np.empty(n), np.empty(n)
m[0] = 1000
f[0] = 600

# (a) System of equations
for t in range(n-1):
	m[t+1] = (1-a_m)*m[t] + k_m*f[t]
	f[t+1] = (1-a_f+k_f)*f[t]

total_members = m + f

# Plot
plt.style.use("seaborn")
plt.plot(n_range, m, label = "Males")
plt.plot(n_range, f, label = "Females")
plt.plot(n_range, total_members, label = "Total Members")
plt.legend()
plt.show()

# (c) Explanation
# The total number of members grows exponentially at a slightly faster rate 
# than the individual populations.
# The sexes eventually cross in population count because females grow at a
# slightly faster rate than males.