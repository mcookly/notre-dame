#!usr/bin/env python
"""
Max Cook
ACMS 40730
Homework 2, Problem 1
"""

import matplotlib.pyplot as plt
from numpy import linspace
import scipy.stats
import math


# Parameters
x_linear = [1.2, 2.5, 3.2, 4.5, 6.7, 8.0, 10.2, 13.1]
y_linear = [3.4851, 78.579, 185.02, 778.54, 3941.8, 11082, 27443, 73185]
x_log = [math.log(x) for x in x_linear]
y_log = [math.log(y) for y in y_linear]

# Create model
data_regress = scipy.stats.linregress(x_log, y_log)
m = data_regress[0]
b = data_regress[1]

# Solve data
x_model_lin = linspace(x_linear[0], x_linear[-1], 100)
y_model_lin = [math.exp(b) * x**m for x in x_model_lin]

# Plot
plt.style.use("seaborn")
fig, (ax1, ax2) = plt.subplots(1, 2)

ax1_data = ax1.scatter(x_linear, y_linear)
ax1_model = ax1.plot(x_model_lin, y_model_lin, c="orange")
ax2_data = ax2.scatter(x_log, y_log)
ax2_model = ax2.plot(x_log, [m*x + b for x in x_log], c="orange")

ax1.set_title("Y vs. X - Linear")
ax2.set_title("Y vs. X - Loglog") # Loglog looks much more linear than semilog

ax1.legend(["Data", "Model"])
ax2.legend(["Data", "Model"])


plt.show()