from sympy import (
    symbols,
    diff,
    integrate,
    Rational,
    lambdify
)

t, v0, g = symbols('t v0 g')
y = v0*t - Rational(1, 2)*g*t**2
dydt = diff(y, t)

print(dydt)

print(r'accelaration', diff(y, t, t))

y2 = integrate(dydt, t)

print(y2)

v = lambdify([t, v0, g], dydt)

print(v(t=0, v0=5, g=9.81))

print(v(2, 5, 9.81))