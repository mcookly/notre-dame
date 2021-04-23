#!/usr/bin/env python3
"""
hw_5_ex_4.py
Maximilian Cook
04.10.2021
"""

# vars
m_import = []
m_sum = []

# import matrices from file
with open("hw_5_ex_4_input.txt", "r") as file:

    for line in file.readlines():
        # m_import's rows = matrix rows. tuples = columns
        m_import.append(tuple(line.rstrip().split(" ")))

# divide import matrix (m_import) into the two matrices
dim_row = (len(m_import) - 1) // 2 # simple way to split into 2 matrices
m1 = m_import[:dim_row]
m2 = m_import[dim_row+1:] # +1 ignores the empty space

with open("hw_5_ex_4_output.txt", "w") as outfile:
    # NOTE: output and calculation combined to optimize script 

    # add matrices together
    for i in range(dim_row):

        row1 = m1[i]
        row2 = m2[i]
        row_sum = []

        for j in range(len(row1)): # could also use row2

            row_sum.append( str(int(row1[j]) + int(row2[j])) )

        # write row's sum
        outfile.write(" ".join(row_sum) + "\n")