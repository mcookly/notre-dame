#!/usr/bin/env python3
"""
hw_3_ex_4.py
Maximilian Cook
03.12.2021
"""

# input
N = int(input("Please enter a positive integer N: "))

# function
def f(n):

    if n == 0:
        return 1

    if n%2 == 0:    # even
        return n // 2
    else:
        return 3*n + 1

def H(k):
    k_total = 0

    while k != 1:
        k = f(k)
        k_total += 1
    
    return k_total

# calculate
sum_H = 0

for k in range(1, N+1):
    sum_H += H(k)

print(f"S({N}) == {sum_H}")