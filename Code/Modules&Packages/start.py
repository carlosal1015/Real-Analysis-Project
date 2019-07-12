from timescale.timescale import Timescale, Timescale_new
import timescale.calculus

from sympy import Rational, S, latex, Symbol
from timescale.core.sigma import sigma, sigma_new
from timescale.core.rho import rho, rho_new
from timescale.core.mu import mu, mu_new
from timescale.core.kappa import T_kappa, T_kappa_new
####################################################
T0 = Timescale([0, Rational(1, 3), Rational(1, 2), Rational(7, 9), 1, 2, 3, 4, 5, 6, 7], 'a')
#x = S("8/9")
print(sigma(T0.ts, 0))
print(sigma(T0.ts, 4))
print(sigma(T0.ts, 7))
print(rho(T0.ts, 1))
print(rho(T0.ts, 2))
print(rho(T0.ts, 0))
print(mu(T0.ts, 0))
####################################################
T = Symbol(r'\mathbb{T}')
T1 = Timescale_new(S.Reals, latex(T) + '=' + latex(S.Reals))
print(sigma_new(T1.ts))
print(rho_new(T1.ts))
print(mu_new(T1.ts))
####################################################
#T2 = Timescale()
####################################################
T3 = Timescale_new()
####################################################

# TODO: Mostrar una menú con conjuntos cerrados (demo).
# TODO: Do definitions (constants): \inf\emptyset == \sup\mathds{T} \wedge \sup\emptyset == \inf\mathds{T}.