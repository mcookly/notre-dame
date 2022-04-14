#!usr/bin/env python
"""
Max Cook
ACMS 40730
Homework 6, Problem 4
"""

import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import numpy as np

# ---------- Parameters

# Constants
MU = 0.02
NU = 0.02
BETA = 1.2
SIGMA = 0.2
GAMMA = 0.15
RHO = 0.1

# Time
t_range = (0, 100)

# ICs : [P, S, E, I, R]
IC = np.array([1e5, 1e5 - 1, 0, 1, 0])

# ---------- Functions

def F(P, S, E, I, R):
	dSdt = MU*P - NU*S - BETA*S*I + RHO*R
	dEdt = -NU*E + BETA*S*I - SIGMA*E
	dIdt = -NU*I + SIGMA*E - GAMMA*I
	dRdt = -NU*R + GAMMA*I - RHO*R
	dPdt = dSdt + dEdt + dIdt + dRdt

	return np.array([dPdt, dSdt, dEdt, dIdt, dRdt])


# ---------- Execute

# Solve IVP
soln = solve_ivp(lambda t, y: F(y[0], y[1], y[2], y[3], y[4]), \
	t_range, IC, method = "Radau", max_step = 1)

# ---------- Plot

plt.style.use("seaborn")
for i in range(5):
	plt.plot(soln.t, soln.y[i])

plt.legend(["Population $P(t)$", "Susceptible $S(t)$", \
	"Exposed $E(t)$", "Infected $I(t)$", "Recovered $R(t)$"])
plt.xlabel("Time $t$")
plt.ylabel("S.E.I.R. Groups and Population")
plt.title("S.E.I.R. Model and Population v. Time")
plt.show()