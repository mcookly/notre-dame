#!/usr/bin/env python3
"""
hw_2_ex_3.py
Maximilian Cook
02.17.2021
"""
# vars
S = 0

# input
N = int(input("Please enter a positive integer N: "))

# sum via for loop
for iN in range(1, N+1):
    S += iN**3
print(f"[for loop] The sum of the cubes from 1 to N is {S}")

# sum via formula
S = 0   # reset

S_a = N * (N + 1)
S = (S_a // 2)**2
print(f"[formula] The sum of the cubes from 1 to N is {S}")