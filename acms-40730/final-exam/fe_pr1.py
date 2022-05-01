#!usr/bin/env python
"""
Max Cook
ACMS 40730
Final Exam, Problem 1
"""

import numpy as np

def find_sd(P: np.array):
	# Found this helpful trick here:
	# https://stackoverflow.com/questions/31791728/python-code-explanation-for-stationary-distribution-of-a-markov-chain

	evals, evecs = np.linalg.eig(P.T)
	evecs1 = evecs[:, np.isclose(evals, 1)]
	evecs1 = evecs1[:,0]
	stationary = evecs1 / evecs1.sum()

	return stationary.real
	
		
## Markov chain named by its corresponding part in the assignment
a = np.array([
	[.2, .8],
	[.3, .7]])

# b is neither irreducible nor aperiodic
# c is irreducible and not aperiodic

d = np.array([
	[.4, .5, .1],
	[.2, .3, .5],
	[.4, .2, .4]])

e = np.array([
	[ 0, .2, .8,  0],
	[.3,  0, .7,  0],
	[ 0, .2, .1, .7],
	[.5,  0,  0, .5]])

# f is neither irreducible nor aperiodic
# g is not irreducible and aperiodic

## Compute
print(f"A: {find_sd(a)}")
print(f"D: {find_sd(d)}")
print(f"E: {find_sd(e)}")