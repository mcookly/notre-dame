#!/usr/bin/env python3
"""
ec_1_ex_2.py
Maximilian Cook
03.26.2021
"""

def replaceWithThreshold(li, threshold):
    # replaces any elements of li that are lower than threshold
    # li: list of integers and/or floats
    # threshold: float

    return [threshold if el < threshold else el for el in li]