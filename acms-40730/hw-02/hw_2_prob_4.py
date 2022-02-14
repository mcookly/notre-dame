#!usr/bin/env python
"""
Max Cook
ACMS 40730
Homework 2, Problem 4
"""

import matplotlib.pyplot as plt

# Functions
def f(u, k):
    u_k3 = u[2] + 3*u[1] + u[0] + pow(k, 2) + k
    return u_k3


def calculate_values(f, N):
    u_values = (N) * [0]
    u_values[:2] = [1, 2, 0]

    if N < 3:
        return u_values[:N+1]
    else:
        for k in range(3, N+1):
            u_values[k] = f(u_values[k-3:k], k)
        return u_values


# Input
N = int(input("Please enter a non-negative integer N: "))

# Execute
u_values = calculate_values(f, N)

# Plot
plt.plot(range(len(u_values)), u_values)
plt.ylabel(r"$u_{k+3}=u_{k+2}+3u_{k+1}+u_k+k^2+k$")
plt.xlabel(r"$k$")
plt.show()