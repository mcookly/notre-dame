#!/usr/bin/env python3
"""
hw_3_ex_2.py
Maximilian Cook
03.12.2021
"""

# functions
def factorial(n):
    total = 1
    for k in range(0, n+1):
        total *= 1 if k == 0 else k

    return total


def cmp_binomial(n_range):
    # row: n
    n_fac = 1           # decided against recalculating factorial values each iteration

    for n in range(0, n_range+1):
        k_fac = 1

        n_fac *= 1 if n == 0 else n

        #print(n_fac)

        for k in range(0, n+1):
            # (n-k)!
            nk_fac = factorial(n-k) # function is used only here to optimize performance

            k_fac *= 1 if k == 0 else k
            binomial = int(n_fac / (k_fac * nk_fac))

            print(f"{binomial :<3}", end=" ")
            # print(n, n_fac, k, k_fac, abs(n-k), nk_fac)
            # print(f"binomial: {binomial}")

        print(end="\n") # terminate line
    return None

# compute

cmp_binomial(10)