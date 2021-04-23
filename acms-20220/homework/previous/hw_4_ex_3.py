#!/usr/bin/env python3
"""
hw_4_ex_3.py
Maximilian Cook
03.26.2021
"""

# function
def replace_with_cumulative_sums(a):
    # DO NOT REASSIGN a

    total = 0

    for i in range(len(a)):
        ia = a[i]
        total += ia
        a[i] = total

# DEBUG <> run
# a = [2, 0, -3, 4, -2]
# print("before:",a)
# replace_with_cumulative_sums(a)
# print('after:', a)