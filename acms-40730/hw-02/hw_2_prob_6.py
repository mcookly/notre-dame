#!usr/bin/env python
"""
Max Cook
ACMS 40730
Homework 2, Problem 6
"""

import math
import numpy as np
import matplotlib.pyplot as plt

def drug_present(t):
	# t -> hours
	M, H, A = 6, 24, 20
	R = math.log(0.5) / H # constant R tuned to half-life time

	return A*(1+t/M) * math.exp(R*t)

# Plot
dp_vec = np.vectorize(drug_present)
t = np.linspace(0, 240, 480)

plt.style.use("seaborn")
plt.plot(t, dp_vec(t))
plt.xlabel("Time t (hours)")
plt.ylabel("Drug Concentration (mg)")
plt.title("Drug Concentration v. Time")
plt.show()