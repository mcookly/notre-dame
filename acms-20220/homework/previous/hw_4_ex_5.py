#!/usr/bin/env python3
"""
hw_4_ex_5.py
Maximilian Cook
03.26.2021
"""

# vars
x = []
y = []
terminate_str = "endinput"
is_x_input = True   # T: x, F: y
str_input = "x"

# input
while True:
    cur_input = input(f"Please enter a value for {str_input}: ")

    # terminate if user inputs it
    if cur_input in terminate_str:
        break

    if is_x_input:
        x.append(float(cur_input))
        is_x_input = False
        str_input = "y"
    else:
        y.append(float(cur_input))
        is_x_input = True
        str_input = "x"
    
# # DEBUG
# x = [1, 3, 7, 9, 2, 5]
# x2 = [1]*6
# y = [3, 6, 2, 18, 7, 9]
# y2 = [1]*6

# function

def least_squares_linreg(x, y):
    # x: sample/list of x values
    # y: sample/list of y values

    print("\n[output]\n")

    # n: length x and y (should be identical lengths)
    n = len(x)

    # check length
    if n != len(y):
        print("Error: Sample sizes of x and y are not identical. Function terminated.")
        return
    elif n == 0 or n == 1:
        print("Error: Sample size must be greater than 1. Function terminated.")
        return

    # calculate sample mean
    x_bar = sum(x) / n
    y_bar = sum(y) / n

    # print sample mean
    print(f"sample mean of x: {x_bar}")
    print(f"sample mean of y: {y_bar}\n")

    # calculate std dev
    x_total = 0.0
    y_total = 0.0

    for i in range(n):
        x_i = x[i]
        y_i = y[i]

        x_total += pow(x_i - x_bar, 2)
        y_total += pow(y_i - y_bar, 2)
    
    x_sdev = pow(x_total / (n-1), 0.5)
    y_sdev = pow(y_total / (n-1), 0.5)

    # print std dev
    print(f"standard deviaton of x: {x_sdev}")
    print(f"standard deviaton of y: {y_sdev}\n")

    # check std dev
    if x_sdev == 0.0:
        print("sample correlation (r): UNDEFINED\n")
        print("least squares regression line: UNDEFINED")
    else:
        if y_sdev == 0.0:
            print("sample correlation (r): UNDEFINED\n")
            print(f"least squares regression line:\n"
                f"ŷ = {y_bar}")
        else:
            # calculate sample correlation 'r'
            r = sum([((x_i-x_bar)/x_sdev) * ((y_i-y_bar)/y_sdev) for x_i in x for y_i in y]) / (n-1)

            # DEBUG
            # print("x_sdev:", x_sdev, "y_sdev:", y_sdev)
            # print("r:", r)
            # calculate least squares reg line
            m = r * (y_sdev / x_sdev)
            b = y_bar - (m * x_bar)

            # sample correlation
            print(f"sample correlation (r): {r}\n")
            # least squares reg line
            print(f"least squares regression line:\n"
            f"ŷ = ({m})x + {b}")

# call function
least_squares_linreg(x, y)