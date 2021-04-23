#!/usr/bin/env python3
"""
ec_1_ex_4.py
Maximilian Cook
04.2.2021
"""

# imports
from math import gcd

# algorithm
"""
suppose a = [1 2 3 4 5 6]
2 - [1 3 5] # so remove 2, 4, and 6
a = [1 3 5]
"""

# function
def relativePrimes(it):
    # finds all ints in li that a relative primes to all other elemens in li
    # SHOULD ONLY ACCEPT NON-ZERO INTS
    # li: iterable of non-zero ints

    it_bool = [True]*len(it) # create boolean list. T: relative prime
    l_it = len(it_bool)

    for i in range(l_it):

        if it_bool[i]:
            # check to see if integer at index i is still True (i.e. unchecked)

            # second for loop can start at index i+1 since previous cases
            # already covered and can ignore itself
            for i2 in range(i+1, l_it):

                # ignore any identical numbers!
                if it[i] != it[i2] and gcd(it[i], it[i2]) != 1:
                    it_bool[i] = False
                    it_bool[i2] = False
                    # print(f"{it[i]} is not relatively prime with {it[i2]}")

    res = set( [it[i3] for i3 in range(l_it) if it_bool[i3]] )
    return res

# DEBUG
# a = [24, 142, 56, 45 , 3, 67, 234, 12, 34, 7, 8, 13]
# print(relativePrimes(a))