#!/usr/bin/env python3
from math import exp

"""
hw_3_ex_1.py
Maximilian Cook
03.12.2021
"""

# function
def taylor_series(x, N):

    # first iteration (allows for k_factorial to compute correctly and not equal 0)
    k_factorial = 1     # must always start at 1
    total = 1 / k_factorial

    for k in range(1, N+1):

        k_factorial *= k
        total += x**k / k_factorial

    return total

# input
N = int(input("Please enter a non-negative integer N: "))
x = float(input("Please enter a value x: "))

# call function
total_sum = taylor_series(x, N)

# output
print()
print(f"Approximated value of exp({x}): {total_sum}")
print(f"True value of exp({x}):         {exp(x)}")