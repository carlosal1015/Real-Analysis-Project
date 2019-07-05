from sympy import Interval, Symbol, oo
#from timescale.timescale import Timescale as tsc
from .rho import rho, sigma_new

def T_kappa(ts, t):
	pass


def T_kappa_new(ts):
	if ts.sup == oo:
		return ts
	else:
		return ts - Interval(rho(ts.sup), ts.sup, left_open = True)