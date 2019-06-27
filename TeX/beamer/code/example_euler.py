#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np
from matplotlib import pyplot as plt

def f(t): return (t**3)/3-t**2

t1 = np.arange(0.0, 4.0, 0.01)

x0, y0, xf, n = 0, 1, 5, 201
deltax = (xf-x0)/(n-1)

x = np.linspace(x0, xf, n)

y = np.zeros([n])
y[0] = 0

for i in range(1, n):
	y[i] = deltax*( x[i - 1]*x[i - 1] - 2*x[i-1] )
	
for i in range(n):
	print(x[i], y[i])

plt.plot(x, y, 'b--',t1, f(t1), 'r--')
plt.xlabel("Valores de x")
plt.ylabel("Valores de y")
plt.title("Solución aproximada con el método de Euler vs la solución exacta")
plt.show()