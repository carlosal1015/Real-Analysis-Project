from scipy import *
#from cmath import sqrt
#print(sqrt(-4))
# polynomial coefficients
a = 1
b = 4
c = 1
from numpy.lib.scimath import sqrt

r1 = (-b + sqrt(b**2 - 4*a*c))/(2*a)
r2 = (-b - sqrt(b**2 - 4*a*c))/(2*a)
print(r1)
print(r2)