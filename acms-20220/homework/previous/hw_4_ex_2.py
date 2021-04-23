#!/usr/bin/env python3
"""
hw_4_ex_2.py
Maximilian Cook
03.26.2021
"""

# function
def find_pair_max(a, b):
    # def: a is a list
    # def: b is a list

    # find the shorter list and assign length n
    if len(a) < len(b):
        n = len(a)
        compared = b
    else:
        n = len(b)
        compared = a

    # compare values
    for i in range(n):

        ia, ib = a[i], b[i]

        compared[i] = ib if ia < ib else ia
    
    return compared

# DEBUG <> run
# a = [0,  2, -5, 3,  7]
# b = [1, 1, 0, 2, 4, 5, -2, 8]
# print(find_pair_max(a, b))