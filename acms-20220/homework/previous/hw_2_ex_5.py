#!/usr/bin/env python3

from math import log

"""
hw_2_ex_5.py
Maximilian Cook
02.25.2021
"""
### functions

def series_at_k(k):
    
    # forumula
    return ((-1)**k) / (k + 2 + log(k**2.5 + 1))

### vars

margin_goal = float(input("Please enter the error margin: "))
series_sum = 0

# initial terms for the while loop
k_1 = series_at_k(1)
k_2 = series_at_k(2)
series_sum = k_1 + k_2
prev_sum = k_2

margin_running = abs(series_sum - prev_sum)     # initial error margin

### calculate
k = 2       # initial k starts at 2 to allow comparison

while margin_running >= margin_goal:
    k += 1  # iterate to new k

    series_sum += series_at_k(k)    # calculate new sum
    margin_running = abs(series_sum - prev_sum)

    prev_sum = series_sum           # hold series sum as now previous sum

print(f"Series is approximately {series_sum} in {k} terms.")