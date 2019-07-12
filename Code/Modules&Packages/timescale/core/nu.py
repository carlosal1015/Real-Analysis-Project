from timescale.timescale import Timescale

def nu(self, t):
	"""
	Función de granicidad minimal:
	.. math::
	\\mu_{\\ast} = \\inf_{\\tau\\in\\left[s,\\infty\right)\\cap\\mathds{T}}\\mu(t).
	"""
	return t - self.rho(t)