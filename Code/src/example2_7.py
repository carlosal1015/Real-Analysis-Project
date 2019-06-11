from sympy import (
    symbols,
    exp, sin, cos,
    latex,
    simplify,
    expand
)

t, v0, g = symbols('t v0 g')

f = exp(t)
print(f)

print(f.series(t, 0, 3))

f = exp(sin(t))
print(f.series(t, 0, 8))

print(latex(f.series(t, 0, 7)))

x, y = symbols('x y')

f = -sin(x)*sin(y) + cos(x)*cos(y)
print(simplify(f))

print(expand(sin(x+y), trig=True))