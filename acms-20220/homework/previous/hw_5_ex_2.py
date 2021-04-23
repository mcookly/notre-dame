#!/usr/bin/env python3
"""
hw_5_ex_2.py
Maximilian Cook
04.10.2021
"""

# functions
def f(x):
    return pow(x,5) - x + 1

def f_prime(x):
    return 5*pow(x,4) - 1

# input
x0 = float(input("Please enter a starting value: "))
err_tol = float(input("Please enter an error tolerance: "))
max_iter = int(input("Please enter a maximum iteration value (int): "))

# vars
x_values = [x0]

# execute
for i in range(max_iter-1):

    xi = x_values[i]

    # check if any stopping conditions are met
    if abs(f(xi)) < err_tol:
        break

    # approximate next x value
    try:
        x_values.append(xi - (f(xi) / f_prime(xi)) )
    except ZeroDivisionError as zde:
        print(f"Error: f'({xi}) == 0. Calculations have stopped.")
        print(zde.args)
        break

# write to file
with open("hw_5_ex_2_output.txt", "w") as outfile:

    for x in x_values:
        outfile.write(f"{x: .16f}\n")