#!/usr/bin/env python3
"""
hw_3_ex_5.py
Maximilian Cook
03.12.2021
"""

# input
N = int(input("Please enter a positive integer N: "))

# vars
total = 0

def f(n):
    #print(n)

    if n <= 2:
        return n
    elif n%2 == 0:
        return (5 * f(n // 2)) + 1
    else:
        return f((n - 1) // 2) + 2

for n in range(1, N+1):
    f_n = f(n)

    if f_n%2 != 0:
        total += f_n

print(f"S({N}) is {total}")