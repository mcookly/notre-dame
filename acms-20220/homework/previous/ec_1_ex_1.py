#!/usr/bin/env python3
"""
exercise_1_ex_1.py
Maximilian Cook
03.29.21
"""
def n_list(li, n):
    # returns a list comprised of li elements of length >= n
    # li: list of strings
    # n: int denoting length to check
    
    return [el for el in li if len(el) >= n]