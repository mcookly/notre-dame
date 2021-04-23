#!/usr/bin/env python3
"""
hw_2_ex_2.py
Maximilian Cook
02.16.2021
"""

# costs
c_apple = 1.00
c_banana = 1.50
c_orange = 0.75
c_lemon = 1.25

# inputs and microbills
print() # empty line

# vars
n_apple = -1
n_banana = -1
n_orange = -1
n_lemon = -1

# apple
while n_apple < 0:
    n_apple = int(input("Please enter the number of apples: "))
total_apple = n_apple * c_apple

if n_apple == 1:
    print(f"The total bill for {n_apple} apple is ${total_apple: 0.2f}")
else:
    print(f"The total bill for {n_apple} apples is ${total_apple: 0.2f}")

# banana
print() # empty line

while n_banana < 0:
    n_banana = int(input("Please enter the number of bananas: "))
total_banana = n_banana * c_banana

if n_banana == 1:
    print(f"The total bill for {n_banana} banana is ${total_banana: 0.2f}")
else:
    print(f"The total bill for {n_banana} bananas is ${total_banana: 0.2f}")

# orange
print() # empty line
while n_orange < 0:
    n_orange = int(input("Please enter the number of oranges: "))
total_orange = n_orange * c_orange

if n_orange == 1:
    print(f"The total bill for {n_orange} orange is ${total_orange: 0.2f}")
else:
    print(f"The total bill for {n_orange} oranges is ${total_orange: 0.2f}")

# lemon
print() # empty line
while n_lemon < 0:
    n_lemon = int(input("Please enter the number of lemons: "))
total_lemon = n_lemon * c_lemon

if n_lemon == 1:
    print(f"The total bill for {n_lemon} lemon is ${total_lemon: 0.2f}")
else:
    print(f"The total bill for {n_lemon} lemons is ${total_lemon: 0.2f}")

# total bill
print() # empty line

print(f"The total number of items purchased is {n_apple+ n_banana+ n_orange+ n_lemon}")
print(f"The overall total bill is ${total_apple+total_banana+total_lemon+total_orange: 0.2f}")