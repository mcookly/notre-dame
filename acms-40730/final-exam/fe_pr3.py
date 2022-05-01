#!usr/bin/env python
"""
Max Cook
ACMS 40730
Final Exam, Problem 3
"""

import numpy as np


### Parameters
N = 100
K = 100
P1 = np.array([
	[.6, .1, .3,  0,  0],
	[.7, .2, .1,  0,  0],
	[.3, .2, .4, .1,  0],
	[.7, .2,  0,  0, .1],
	[ 0,  0,  0,  0,  1]])


### Functions
def journey_stepwise(s: int, P: np.array):
	# Indices are handled numerically as 0–3, while states are 1–4

	cur_state_index = s-1 # Index from state no.
	x0 = np.zeros(4)
	x0[cur_state_index] = 1 # Initial state
	visited_states = np.zeros(K+1)

	# print(f"Starting from State {s}")
	for k in range(K):
		# print(f"	Current probabilities: {P[cur_state_index,:]}")
		next_state_index = rnp.choice(4, p=P[cur_state_index,:])
		cur_state_index = next_state_index
		visited_states[k] = cur_state_index + 1
		# print(f"	Chose State {next_state_index+1}")
	
	# print(f"Visited states: {visited_states}\n")
	return visited_states