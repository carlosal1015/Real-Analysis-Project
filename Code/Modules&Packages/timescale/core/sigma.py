"""
Función salto hacia adelante
=========================

This module implements an algorithm for generation of forward jump for time scales.

The core algorithm is provided in the finite difference weight generating
function (``finite_diff_weights``), and two convenience functions are provided
for:

- estimating a derivative (or interpolate) directly from a series of points
    is also provided (``apply_finite_diff``).
- differentiating by using finite difference approximations
    (``differentiate_finite``).
"""
from sympy import Interval, Symbol, oo
#from timescale.timescale import Timescale as tsc

def sigma(ts, t):
	"""

	.. math::
	\\sigma(t) = \\inf \\{z\\in\\mathds{T} : z>t \\}

	Parameters
    ==========

	derivative: a Derivative instance
    points: sequence or coefficient, optional
        If sequence: discrete values (length >= order+1) of the
        independent variable used for generating the finite
        difference weights.
        If it is a coefficient, it will be used as the step-size
        for generating an equidistant sequence of length order+1
        centered around ``x0``. default: 1 (step-size 1)
    x0: number or Symbol, optional
        the value of the independent variable (``wrt``) at which the
        derivative is to be approximated. Default: same as ``wrt``.
    wrt: Symbol, optional
        "with respect to" the variable for which the (partial)
        derivative is to be approximated for. If not provided it
        is required that the Derivative is ordinary. Default: ``None``.


	Examples
    ========

	>>> from sympy import S
    >>> from sympy.calculus import finite_diff_weights
    >>> res = finite_diff_weights(1, [-S(1)/2, S(1)/2, S(3)/2, S(5)/2], 0)
    >>> res

	Notes
    =====

    If weights for a finite difference approximation of 3rd order
    derivative is wanted, weights for 0th, 1st and 2nd order are
    calculated "for free", so are formulae using subsets of ``x_list``.
    This is something one can take advantage of to save computational cost.
    Be aware that one should define ``x_list`` from nearest to farest from
    ``x0``. If not, subsets of ``x_list`` will yield poorer approximations,
    which might not grand an order of accuracy of ``len(x_list) - order``.

    See also
    ========

    sympy.calculus.finite_diff.apply_finite_diff

    References
    ==========

    .. [1] Generation of Finite Difference Formulas on Arbitrarily Spaced
            Grids, Bengt Fornberg; Mathematics of computation; 51; 184;
            (1988); 699-706; doi:10.1090/S0025-5718-1988-0935077-0

	"""
	# pass
	tIndex = 0
	tNext = None
	iterations = 0

	for x in ts:
		if (not isinstance(x, list) and t == x) or (isinstance(x, list) and t >= x[0] and t <= x[1]):
			tIndex = iterations
			break

		iterations = iterations + 1

	if (tIndex + 1) == len(ts):
		return t

	elif isinstance(ts[tIndex], list):
		if (t != ts[tIndex][1]):
			return t

		else:
			if (isinstance(ts[tIndex + 1], list)):
				return ts[tIndex + 1][0]

			else:
				return ts[tIndex + 1]

	else:
		tNext = ts[tIndex + 1]

		if isinstance(tNext, list):
			return tNext[0]

		else:
			return tNext


def sigma_new(ts):
	if ts.open == True:
		infimum = None
		return infimum # Not is the case, until the is_closed () method is created.
	else:
		t = Symbol('t')
		# Assume that ts == \mathbb{R}
		condition = ts.intersect(Interval(t, oo, left_open = True))
		return condition.inf