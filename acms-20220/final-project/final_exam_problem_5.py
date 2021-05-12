#!/usr/bin/env/ python3

import numpy as np
"""
Problem 5 in ACMS 20220 Final
Author: Max Cook
Date: 05/08/2021 (Modified: 05/12/2021)
See 'Problem 5' for the algorithm:
https://lucid.app/lucidchart/invitations/accept/inv_9370e3fa-6a2a-409a-b9b0-7dd45eba7da3?viewport_loc=-121%2C348%2C1724%2C673%2C0_0
"""

with open("final_exam_problem_5_input.txt", "r") as file:
    board = []
    for line in file:
        row = [int(num) for num in line.rstrip().rsplit(",")]
        board.append(row)
    board = np.array(board)
    # Convert to numpy array for easier indexing
    # and vectorized array additions.

# Iterate through rows of the board, starting from second 
# from bottom (destination).
cur_square_sums = board[-1].copy()
# A 1D array that remembers the greatest score per each point in the row.
for i in reversed(range(board.shape[0]-1)):
    cur_row = board[i].copy()
    best_paths = np.zeros(board.shape[1], dtype="int64")
    for j in range(len(cur_row)):
        # I could use 'range(board.shape[1])' as well, but I don't see any 
        # reason for doing that.
        left_square = -1
        middle_square = -1
        right_square = -1

        if j == 0:
            # Left edge of board requires 2 checks only: DOWN and RIGHT
            middle_square = cur_square_sums[j]
            right_square = cur_square_sums[j+1]
        elif j == len(cur_row) - 1:
            # Right edge of board requires cks only: DOWN and LEFT
            left_square = cur_square_sums[j-1]
            middle_square = cur_square_sums[j]
        elif j < len(cur_row) - 1:
            # Non-edge square requires 3 checks: LEFT, DOWN, and RIGHT
            left_square = cur_square_sums[j-1]
            middle_square = cur_square_sums[j]
            right_square = cur_square_sums[j+1]

        best_paths[j] = max(left_square, middle_square, right_square)
    cur_square_sums = best_paths + cur_row

print(cur_square_sums)