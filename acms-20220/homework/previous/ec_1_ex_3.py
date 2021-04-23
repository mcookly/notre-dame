#!/usr/bin/env python3
"""
ec_1_ex_3.py
Maximilian Cook
03.31.2021
"""

def NotDivisible(li_1, li_2):
    # returns a list of integers in li_1 that cannot be /
    # divided by any elements in li_2
    # li_1: list of ints
    # li_2: list of ints

    res = []

    for el in li_1:
        passes = True  

        for el_2 in li_2:
            if el_2 != 0 and el % el_2 == 0:
                passes = False
                break
        
        if passes:
            res.append(el)

    return res

# DEBUG
# a = [10, 26, 45, 56, 78, 98, 34, 35, 37, 43]
# b = [0, 2, 3, 6, 8, 17, 23]
# print(NotDivisible(a, b))