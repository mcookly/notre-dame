#!usr/bin/env python
"""
Max Cook
ACMS 40730
Final Exam, Problem 6
"""

import numpy as np


### Parameters 
rnp = np.random.default_rng()
K = 6
N = 100000
P = np.array([
	[.1, .2, .5, .2],
	[.4, .1, .5, .0],
	[.3, .3, .3, .1],
	[.2, .5, .1, .2]])


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


def N_update(state, cur_n):
	if cur_n%(N/10) == 0:
		print(f"[State {state}]: Completed {cur_n} of {N} trials ...")
	else:
		pass


### Calculate

for i in range(1, 5):
	num_returned = 0
	for n in range(N):
		N_update(i, n)
		visited = journey_stepwise(i, P)
		num_returned += 1 if i in visited else 0
	print(f"Probabiliy of returning to State {i}: {round(1-num_returned/N, 4)}")