#!/usr/bin/env python3

import math

"""
hw_3_ex_3.py
Maximilian Cook
03.12.2021
"""

# input
N = int(input("Please enter a non-negative integer N: "))

# function
def isprime(i): # N.B. does not work for negative integers

    if i == 1:
        return True
    
    for factor in range(2, math.floor(math.sqrt(i))+1):
        if i % factor == 0:
            return False
    
    return True

for n in range(1, N+1):
    if isprime(n) == True:
        print(f"{n} is prime.")
    else:
        print(f"{n} is not prime.")