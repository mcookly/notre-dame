#!/usr/bin/env python3
"""
hw_5_ex_3.py
Maximilian Cook
04.10.2021
"""

# vars
f_names = set()
text = str()
let_cnts = dict()
total_cnt = 0
alphabet = "abcdefghijklmnopqrstuvwxyz"

# receive filenames
while True:
    f_name = input("Please enter a filename or dir: ")

    if "endinput" in f_name:
        break

    # add to filenames
    f_names.add(f_name)

# load files and gather letters
for f in f_names:

    try:
        with open(f, "r") as file:
            for line in file:
                piece = line.strip()
                text += piece.lower()
    except FileNotFoundError as fnfe:
        print(f"\nERROR: unable to find/open '{f}'")

# IF no files are listed
if not text:
    print(f"No files were processed. Exiting program...")
    exit()

# count letters
for letter in alphabet:

    let_cnt = text.count(letter)
    total_cnt += let_cnt # always update this
    if letter in let_cnts:
        let_cnts[letter] += let_cnt
    else:
        let_cnts[letter] = let_cnt

# output
print("\nLetter   |Count   |Frequency (%)\n")
for letter, count in let_cnts.items():

    freq = (count / total_cnt) * 100
    print(f"{letter :<10}{count :<8}{freq: .2f}")