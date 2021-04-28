#!/usr/bin/env python3

# modules
import numpy as np

"""
filename:   ode.py
author:     Maximilian Cook
date:       04/26/2021
summary:    approximates an ODE  over [0, b] using Euler's method
"""

# function
def eulers_method(f, y0=np.double(0), b=np.double(1), n=1):
    # f: f(x, y)
    # y0: starting value (y) of approximation
    # b: endpoint (x) of approximation
    # n: number of subintervals

    # initial values
    # NOTE. using n+1 instead of n to match output. Not sure why it's needed.
    x = [0]*(n+1)
    y = [y0]*(n+1)

    # divide interval [0, b] into subintervals h
    h = b / n

    # approximate
    for i in range(n):
        xi = x[i]
        yi = y[i]

        # next values
        x[i+1] = xi + h
        y[i+1] = yi + (h * f(xi, yi))
    
    return list(zip(x, y))