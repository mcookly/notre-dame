#!/usr/bin/env python3
"""
hw_5_ex_1.py
Maximilian Cook
04.10.2021
"""

# open file of integers
with open('hw_5_ex_1_input.txt', 'r') as file:

    totals = []

    # iterate through each line in the file
    for line in file.readlines():
        
        # split ints by ';'
        integers_str = line.rstrip()

        # makes sure line is not empty
        if integers_str:
            integers_str = integers_str.split(';')
            integers = [int(i) for i in integers_str if i]

            # add total to list for writing
            totals.append(sum(integers))

# write output of sums
with open('hw_5_ex_1_output.txt', 'w') as outfile:

    # iterate through totals
    for total in totals:
        outfile.write(f'{total}\n')