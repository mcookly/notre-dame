# !/usr/bin/env/ python3

"""
Problem 3 on ACMS 20220 Final
Author: Max Cook (Collab: Nick Clark)
Date: 05/12/2021 (Modified:)
"""

import numpy as np

with open("final_exam_problem_3_input_5.txt", "r") as file:
    lines = file.readlines()
    DIM = int(lines[0].rstrip())
    NUM_TRIALS = int(lines[1].rstrip())

rng = np.random.default_rng(seed = 1234)
target_pos = (DIM-1, 0)
total = 0

# Debug function
def board_vis(dim, old_position, new_position):
    print(f"\n\nFrom {old_position} to {new_position}")
    for i in range(dim):
        row_str = ""
        for j in range(dim):
            if i == old_position[0] and j == old_position[1]:
                row_str += "X "
            elif i == new_position[0] and j == new_position[1]:
                row_str += "P "
            else:
                row_str += "_ "
        print(row_str)  

# Knight moves
def rand_move(cur_pos):
    """
    cur_pos: 2D tuple
    """

    # NOTE. Assuming the L-shape is row-1 and col+3 for horizontal
    # and row-3 and col+1 for vertical.

    row, col = cur_pos[0], cur_pos[1]
    l_shape = np.random.randint(2) # 1: turns R, 0: turns L
    compass = np.random.randint(1,5) # E: 1, N: 2, W: 3, S: 4
    
    # Determines next position
    if compass == 1: # East
        col += 2
        row += 1 if l_shape else -1
    elif compass == 2: # North
        col += 1 if l_shape else -1
        row -= 2
    elif compass == 3: # West
        col -= 2
        row -= 1 if l_shape else -1
    elif compass == 4: # South
        col -= 1 if l_shape else -1
        row += 2
    return row, col

pos = target_pos
for _ in range(NUM_TRIALS):
    while True:
        new_pos = rand_move(pos)
        if 0 <= new_pos[0] < DIM and 0 <= new_pos[1] < DIM:
            #board_vis(DIM, pos, new_pos)
            total += 1
            pos = new_pos
            if pos == target_pos:
                break
print(total / NUM_TRIALS)