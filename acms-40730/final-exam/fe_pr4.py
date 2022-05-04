#!usr/bin/env python
"""
Max Cook
ACMS 40730
Final Exam, Problem 4
"""

import numpy as np

### Functions
def long_term(P: np.array):
	output_indices = [1, 10, 1000]
	for i in output_indices:
		print(f"P^{i}:\n{np.linalg.matrix_power(P, i)}\n")

### Transition matrices
a = np.array([
	[.9, .1],
	[.8, .2]])

b = np.array([
	[1, 0],
	[0, 1]])

c = np.array([
	[0, 1],
	[1, 0]])

d = np.array([
	[ 1,  0,  0],
	[.5,  0, .5],
	[ 0,  0,  1]])

e = np.array([
	[.5, .5,  0],
	[.4, .4, .2],
	[ 0,  0,  1]])

### Run
long_term(e)
