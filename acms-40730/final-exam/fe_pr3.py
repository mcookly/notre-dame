#!usr/bin/env python
"""
Max Cook
ACMS 40730
Final Exam, Problem 3
Note: These Monte Carlo algorithms are incredibly slow.
"""

import numpy as np


### Parameters
rnp = np.random.default_rng()
N = 10000 # no. of trials
K = 10000 # no. of steps
# NOTE: K > 10000 or the simulation breaks down
P1 = np.array([
	[.6, .1, .3,  0,  0],
	[.7, .2, .1,  0,  0],
	[.3, .2, .4, .1,  0],
	[.7, .2,  0,  0, .1],
	[ 0,  0,  0,  0,  1]])

P2 = np.array([
	[.2, .1, .4,  0, .3],
	[.5, .4,  0,  0, .1],
	[.2,  0, .6, .1, .1],
	[ 0,  0,  0,  1,  0],
	[ 0,  0,  0,  0,  1]])


### Functions
def journey_stepwise(s: int, P: np.array):
	# Indices are handled numerically as 0–3, while states are 1–4

	cur_state_index = s-1 # Index from state no.
	num_steps = 1

	while cur_state_index+1 != 5:
	# print(f"Starting from State {s}")
		cur_state_index = rnp.choice(P.shape[0], p=P[cur_state_index,:])
		num_steps += 1

	return num_steps

	# Old code ----
	# for k in range(1, K+1):
	# 	# print(f"	Current probabilities: {P[cur_state_index,:]}")
	# 	next_state_index = rnp.choice(P.shape[0], p=P[cur_state_index,:])
	# 	# print(f"On state {next_state_index+1}")
	# 	if next_state_index+1 == 5:
	# 		# print(f"Found State 5 after {k} steps")
	# 		return k
	# 	else:
	# 		cur_state_index = next_state_index
	# 	# print(f"	Chose State {next_state_index+1}")
	
	# print(f"Visited states: {visited_states}\n")
	# return 0


def journey_prob(s: int, P: np.array):
	# Indices are handled numerically as 0–3, while states are 1–4

	cur_state_index = s-1 # Index from state no.
	x0 = np.zeros(P.shape[0])
	x0[cur_state_index] = 1 # Initial state

	# print(f"Starting from State {s}")
	for k in range(K):
		# print(f"	Current probabilities: {P[cur_state_index,:]}")
		next_state_index = rnp.choice(P.shape[0], p=P[cur_state_index,:])
		# print(f"On state {next_state_index+1}")
		if next_state_index+1 == 5:
			# print(f"Found State 5 after {k} steps")
			return 5
		elif next_state_index+1 == 4:
			return 4
		else:
			cur_state_index = next_state_index
		# print(f"	Chose State {next_state_index+1}")
	
	# print(f"Visited states: {visited_states}\n")
	return 0


def N_update(state, cur_n):
	if cur_n%(N/10) == 0:
		print(f"[State {state}]: Completed {cur_n} of {N} trials ...")
	else:
		pass

### Calculate no. timesteps using Monte Carlo method for P1
for i in range(1, 5):
	# Run through states 1–4
	sum_steps = 0
	# mistrials = 0
	for n in range(N):
		N_update(i, n)
		sum_steps += journey_stepwise(i, P1)
		# mistrials += 1 if sum_steps == 0 else 0

	print(f"Expected number of timesteps from State {i} to State 5: {sum_steps/N}")

### Calculate probabilites of landing in States 4 and 5 of P2
# for i in range(1, 4):
# 	# Run through states 1–3
# 	sum_reaches = np.zeros(2) # [reach 4, reach 5]
# 	mistrials = 0
# 	for n in range(N):
# 		N_update(i, n)

# 		hit = journey_prob(i, P2)

# 		if hit == 5:
# 			sum_reaches[1] += 1
# 		elif hit == 4:
# 			sum_reaches[0] += 1
# 		else:
# 			mistrials += 1

# 	print(f"The probability of State 4 absorbing the chain from State {i}: {sum_reaches[0]/(N-mistrials)}")
# 	print(f"The probability of State 5 absorbing the chain from State {i}: {sum_reaches[1]/(N-mistrials)}\n")