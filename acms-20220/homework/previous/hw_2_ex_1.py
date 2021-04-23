#!/usr/bin/env python3
"""
hw_2_ex_1.py
Maximilian Cook
02.16.2021
"""

# input

int_1 = int(input("Enter 1/3 of integers: "))
int_2 = int(input("Enter 2/3 of integers: "))
int_3 = int(input("Enter 3/3 of integers: "))

# vars for sorting

sma = int_1
med = int_2
lar = int_3

# sort

if int_1 <= int_2:
     # is (1) <= (2)?

    if int_3 <= int_1:
        # (3) <= (1) <= (2)
        sma = int_3
        med = int_1
        lar = int_2
    elif int_3 <= int_2:
        # (1) <= (3) <= (2)
        sma = int_1 # default
        med = int_3
        lar = int_2
    # else: (1) <= (2) <= (3). this is the default preset


elif int_2 <= int_1:
    # if not, is (2) <= (1)?
    
    if int_3 <= int_2:
        # (3) <= (2) <= (1)
        sma = int_3
        med = int_2
        lar = int_1
    elif int_3 <= int_1:
        # (2) <= (3) <= (1)
        sma = int_2
        med = int_3
        lar = int_1
    else:
        # (2) <= (1) <= (3)
        sma = int_2
        med = int_1
        lar = int_3

print() # new line
print(f"Smallest int: {sma}\n"
      f"Middle int: {med}\n"
      f"Largest int: {lar}")