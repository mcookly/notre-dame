#!/usr/bin/env python3
"""
hw_5_ex_5.py
Maximilian Cook
04.10.2021
"""

# vars
terms = []

# functions
def cf_expand_iterative(a):
    # a: a0, ..., an

    frac = a[-1] # began with final a
    for i in reversed(range(len(a)-1)):
        # slowly add next terms
        frac = a[i] + pow(frac, -1)

    return frac

def cf_expand_recursive(a):
    
    # STOP condition
    if len(a) == 1:
        return pow(a[0], -1)
    else:
        return a[0] + pow(cf_expand_recursive(a[1:]), -1)

# read files
with open("hw_5_ex_5_input.txt", "r") as file:
    for line in file.readlines():

        line2 = [] # intermediary line
        line = line.rstrip().split(";") # remove newline characters

        # add all components of line to line2 and make a one-level list
        line2.append(line[0])
        line2.extend(line[1].split(","))

        terms.append( [int(a) for a in line2] )

# calculate and write into file
with open("hw_5_ex_5_output.txt", "w") as outfile:

    for term in terms:
        outfile.write(f"{cf_expand_iterative(term) :.16f}\n")