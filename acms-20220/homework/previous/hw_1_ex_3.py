#!/usr/bin/env python3
"""
hw_1_ex_3.py
Maximilian Cook
02.09.21
"""

# costs
c_apple = 1.00
c_banana = 1.50
c_orange = 0.75
c_lemon = 1.25

# inputs and microbills
print() # empty line

# apple
n_apple = int(input("Please enter the number of apples: "))
total_apple = n_apple * c_apple
print(f"The total bill for {n_apple} apple(s) is ${total_apple: 0.2f}")

# banana
print() # empty line
n_banana = int(input("Please enter the number of bananas: "))
total_banana = n_banana * c_banana
print(f"The total bill for {n_banana} banana(s) is ${total_banana: 0.2f}")

# orange
print() # empty line
n_orange = int(input("Please enter the number of oranges: "))
total_orange = n_orange * c_orange
print(f"The total bill for {n_orange} orange(s) is ${total_orange: 0.2f}")

# lemon
print() # empty line
n_lemon = int(input("Please enter the number of lemons: "))
total_lemon = n_lemon * c_lemon
print(f"The total bill for {n_lemon} lemon(s) is ${total_lemon: 0.2f}")

# total bill
print() # empty line

print(f"The total number of items purchased is {n_apple+ n_banana+ n_orange+ n_lemon}")
print(f"The overall total bill is ${total_apple+total_banana+total_lemon+total_orange: 0.2f}")