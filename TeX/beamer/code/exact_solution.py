#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 12:19:22 2019

@author: User
"""

import numpy as np
from matplotlib import pyplot as plt

def f(t):
	return 0.5*(3*np.exp(-t)+np.sin(t)-np.cos(t))

t1 = np.arange(0.0, 10.0, 0.1)

plt.plot(t1, f(t1), 'r--')
plt.xlabel("Value of x")
plt.ylabel("Value of y")
plt.title("Solución exacta del PVI.")
plt.show()