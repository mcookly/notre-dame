#!/usr/bin/env/ python3

"""
Problem 3 on ACMS 20220 Final
Author: Max Cook (Collab: Nick Clark)
Date: 05/12/2021 (Modified: 05/14/2021)
"""

import numpy as np

with open("final_exam_problem_3_input.txt", "r") as file:
    # NOTE: Filename should be "final_exam_problem_3_input.txt"
    lines = file.readlines()
    DIM = int(lines[0].rstrip())
    NUM_TRIALS = int(lines[1].rstrip())

rng = np.random.default_rng()
target_pos = (DIM-1, 0)

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
    move_choice = np.random.randint(1,9)
    l_orient = 1 # 1: R, -1: L
    row_step = 0 # 1: EW, 2: NS
    col_step = 0 # 2: EW, 1: NS
    # (1–4): ER, NR, WR, SR; (1–8): EL, NL, WL, SL

    l_orient = 1 if move_choice <= 4 else -1
    # Knight moves in a right L-shape or left L-shape
    if move_choice in (1, 5): # East
        col_step = 2
        row_step = l_orient
    elif move_choice in (2, 6): # North
        col_step = l_orient
        row_step = -2
    elif move_choice in (3, 7): # West
        col_step = -2
        row_step = -l_orient
    elif move_choice in (4, 8): # South
        col_step = -l_orient
        row_step = 2

    row += row_step
    col += col_step
    return row, col

def is_valid_position(pos, dim):
    return min(pos) >= 0 and max(pos) < dim

total = 0
pos = target_pos
for _ in range(NUM_TRIALS):
    moves = 0
    while True:
        new_pos = rand_move(pos)
        while not is_valid_position(new_pos, DIM):
            new_pos = rand_move(pos)
        # board_vis(DIM, pos, new_pos)
        moves += 1
        pos = new_pos
        if pos == target_pos:
            break
    total += moves
print(total / NUM_TRIALS)