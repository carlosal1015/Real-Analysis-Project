from sympy import Interval, Symbol, oo
#from timescale.timescale import Timescale as tsc
from .sigma import sigma, sigma_new

def mu(ts, t):
	"""
	Función de granicidad:
	.. math::
		\\mu(t) = \\sigma(t) - t
	"""
	pass

	for x in ts:
		if isinstance(x, list) and t >= x[0] and t < x[1]:
			return 0

		return sigma(ts, t) - t


def mu_new(ts):
	t = Symbol('t')
	return sigma_new(ts) - t