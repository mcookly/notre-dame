#!/usr/bin/env python3
"""
hw_4_ex_4.py
Maximilian Cook
03.26.2021
"""

# vars
names = []
scores = []
terminate_string = "endinput"

# input
while True:
    name = input("Please enter a student's name: ")

    # STOP if name is already entered or termination string inputted
    if (name in names) or (name == terminate_string):
        break

    score = int(input("Please enter their score: "))

    # STOP if score is out of range
    if not (0 <= score <= 100):
        break

    names.append(name)
    scores.append(score)

# find maximum and minmum scores

# find max & min score
max_score = max(scores)
min_score = min(scores)

max_score_indeces = [i for i in range(len(scores)) if scores[i] == max_score]
min_score_indeces = [i for i in range(len(scores)) if scores[i] == min_score]

# print
print(f"\nThe highest exam score is {max_score}. Student(s) who scored {max_score}:")
for i_max in max_score_indeces:
    print("    ", names[i_max])

print(f"\nThe lowest exam score is {min_score}. Student(s) who scored {min_score}:")
for i_min in min_score_indeces:
    print("    ", names[i_min])