#!usr/bin/env python
"""
Max Cook
ACMS 40730
Final Exam, Problem 2
"""

import numpy as np

### Parameters
nyears = 4
states = ["Drought", "Low", "Medium", "Heavy"]

# Markov chain transition matrix
P = np.array([
	[.2, .3, .4, .1],
	[.3, .2, .4, .1],
	[.1, .2, .4, .3],
	[.2, .2, .4, .2]])

# initial stochastic vector
x0 = np.array([
	[1, 0, 0, 0],
	[0, 1, 0, 0],
	[0, 0, 1, 0],
	[0, 0, 0, 1]])

### Functions
def calc_markov(x0: np.array, nt: int, state: str, f):
	f.write(f"\n--- Current Year: {state} ---\n")

	y = x0
	for t in range(nt):
		y = y @ P
		f.write(f"+ {t+1} Year(s): {y}\n")


### Calculate

## Probabilities
f = open("fe_pr2_output.txt", "w")
for i in range(4):
	calc_markov(x0[i], 4, states[i], f)
f.close()

## Stationary Distribution
evals, evecs = np.linalg.eig(P.T)
evecs1 = evecs[:, np.isclose(evals, 1)]
evecs1 = evecs1[:,0]
stationary = evecs1 / evecs1.sum()
print(stationary.real)