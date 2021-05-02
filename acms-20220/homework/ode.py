#!/usr/bin/env python3

import numpy as np

"""
filename:   ode.py
author:     Maximilian Cook
date:       04/26/2021
summary:    approximates an ODE  over [0, b] using Euler's method
"""

def eulers_method(f, y0=np.double(0), b=np.double(1), n=1):
    # f: f(x, y)
    # y0: starting value (y) of approximation
    # b: endpoint (x) of approximation
    # n: number of subintervals

    # NOTE. using n+1 instead of n to match output. Not sure why it's needed.
    x = [0]*(n+1)
    y = [y0]*(n+1)
    h = float(b / n)
    # Use Euler's method to approximate next temrms
    for i in range(n):
        xi = x[i]
        yi = y[i]
        x[i+1] = xi + h
        y[i+1] = yi + (h * f(xi, yi))
    return list(zip(x, y))