#!/usr/bin/env python3
"""
hw_2_ex_4.py
Maximilian Cook
02.18.2021
"""
# vars
S = 0   # sum

# input
N = int(input("Please enter a positive integer N: "))

# calculate
for iN in range(1, N+1):
    cond_1 = iN % 2
    cond_2 = iN % 5
    cond_3 = iN % 10    # avoid this condition

    if (cond_3 != 0) and ((cond_1 == 0) or (cond_2 == 0)):
        S += iN

# output
print(f"The sum is {S}")