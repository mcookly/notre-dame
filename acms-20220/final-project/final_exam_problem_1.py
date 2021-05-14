# !/usr/bin/env/ python3

"""
Problem 1 in ACMS 20220 Final
Author: Max Cook (Collab: Nick Clark)
Date: 05/12/2021
"""

import numpy as np

with open("final_exam_problem_1_input.txt", "r") as file:
    # NOTE: Make sure to adjust to "final_exam_problem_1_input.txt"
    lines = file.readlines()
    POINT = tuple([float(x) for x in lines[0].rstrip().split(",")])
    # Point from which distance will be compared in the sphere.
    DIM = len(POINT)
    # Dimension can be any non-zero number
    NUM_TRIALS = int(lines[1].rstrip())
    # Number of trials for Monte Carlo method

# Monte Carlo method
total = 0
rng = np.random.default_rng()
for _ in range(NUM_TRIALS):
    x = rng.uniform(-1.0, 1.0, DIM)
    while not np.linalg.norm(x) <= 1:
        # While point x is not inside the unit sphere
        x = rng.uniform(-1.0, 1.0, DIM)
    total += np.linalg.norm((POINT, x))

print(total/NUM_TRIALS)