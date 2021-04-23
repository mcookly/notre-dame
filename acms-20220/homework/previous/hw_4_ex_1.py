#!/usr/bin/env python3
"""
hw_4_ex_1.py
Maximilian Cook
03.26.2021
"""

# function

def squares_mod_n(n):

    # stop function if n is not positive
    if n <= 0:
        return None

    n_use = n-1 if n%2 != 0 else n # simplifies the indexing and removes possible rounding errors

    # calculate squares
    squares = [(x**2)%n for x in range(0,n+1)]

    # sort
    squares = sorted(squares[:n_use//2+1]) # pattern indicates that just half the list is needed

    # ideal return
    return squares


# DEBUG <> run
# n_input = int(input("Please enter a positive integer: "))
# print(squares_mod_n(n_input))