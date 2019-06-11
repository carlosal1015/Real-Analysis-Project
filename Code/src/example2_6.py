from sympy import (
    symbols,
    Rational,
    solve
)
t, v0, g = symbols('t v0 g')
y = v0*t - Rational(1, 2)*g*t**2

roots = solve(y, t)

print(roots)

print(y.subs(t, roots[0]))

print(y.subs(t, roots[1]))