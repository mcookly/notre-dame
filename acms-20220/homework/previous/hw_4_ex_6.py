#!/usr/bin/env python3
"""
hw_4_ex_6.py
Maximilian Cook
03.26.2021
"""

# function
def phi(k):
    # k: number of terms

    # for the case phi(1) == 1
    if k == 1:
        return 1

    # create list of all ints between 1 and k
    coprimes = [True]*(k)
    coprimes[0] = False     # ignore case. Simply used for indexing

    # remove cofactors (1 will always be a coprime)
    for i in range(2,8):
        coprime = i

        if k%coprime == 0:
            #print("Found coprime: ",coprime)
            for j in range(i, k, coprime):
                #print(f"Deleting {j}")
                coprimes[j] = False

    # print('k:', k)
    # print([i for i in range(k) if coprimes[i]]) # <-- use to check if function works
    # print(coprimes.count(True))
    return coprimes.count(True)

# run
n = int(input("Please enter a positive integer n: "))
total = sum([phi(k) for k in range(1, n+1)])
print(f"S({n}) == {total}")