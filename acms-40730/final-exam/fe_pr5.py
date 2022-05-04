#!usr/bin/env python
"""
Max Cook
ACMS 40730
Final Exam, Problem 5
"""

from random import random
import numpy as np
from scipy import rand

### Parameters
N = 10000
K = 200

### Read matrix
with open("final_exam_problem_5_input.txt", "r") as f:
	# NOTE: File name for submission needs to be "final_exam_problem_5_input.txt"
	flines = f.readlines()

dim = len(flines)
P = np.empty((dim, dim)) # Creates the correct dimension P

for i in range(dim):
	P[i,:] = [float(n) for n in flines[i].strip().split(",")]


### Estimate using Monte Carlo method
statdist_sum = 0
for n in range(N):
	# Select random state to begin the chain
	x0 = np.zeros(dim)
	x0[np.random.randint(0, dim)] = 1
	statdist_sum += x0 @ np.linalg.matrix_power(P, K)

print(f"The estimated Stationary Distribution of P is: {statdist_sum/N}")