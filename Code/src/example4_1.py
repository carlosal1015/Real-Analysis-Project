def diff2nd(f, x, h=1E-6):
    r = (f(x-h) - 2*f(x) + f(x+h))/float(h*h)
    return r


f = lambda x: x**2 + 4

"""
Equivalent to
def f(x):
    return x**2
"""