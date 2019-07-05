from sympy import Interval, Symbol, oo
#from timescale.timescale import Timescale as tsc

def rho(ts, t):
	"""
	Función Salto hacia atrás:
	.. math::
	\\rho(t) = \\sup \\{ z\\in\\mathds{T} : z<t \\}
	"""
	if t == min(ts):
		return t
	else:
		return max([x for x in ts if x < t])


def rho_new(ts):
	if ts.open == True:
		supremum = None
		return supremum # Not is the case, until the is_closed () method is created.
	else:
		t = Symbol('t')
		# Assume that ts == \mathbb{R}
		condition = ts.intersect(Interval(-oo, t, right_open = True))
		return condition.sup