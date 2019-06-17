from timescale.classes.timescale import Timescale
from timescale.integration.integration import *
import numpy as np

"""
	Cylinder transformation from definition 2.21
"""
def cyl(self, t, z):
	if (self.mu(t) == 0):
		return z
	
	else:
		return 1/self.mu(t) * np.log(1 + z*self.mu(t))

"""
	Delta exponential based on definition 2.30
"""
def dexp_p(self, p, t, s):        
	def f(t):
		return self.cyl(t, p(t))

	return np.exp(self.dintegral(f, t, s))


"""
	forward circle minus
"""
def mucircleminus(self,f,t):
	return -f(t)/(1+f(t)*self.mu(t))

"""
	The forward-derivative cosine trigonometric function.
"""

def dcos_p(self, p, t, s):
	dexp_p1 = self.dexp_p(lambda x: p(x) * 1j, t, s)

	dexp_p2 = self.dexp_p(lambda x: p(x) * -1j, t, s)

	result = ((dexp_p1 + dexp_p2) / 2)
	
	if np.imag(result) == 0:
		return np.real(result)
	
	else:
		return result


"""
	The forward-derivative sine trigonometric function.
"""
def dsin_p(self, p, t, s):
	dexp_p1 = self.dexp_p(lambda x: p(x) * 1j, t, s)

	dexp_p2 = self.dexp_p(lambda x: p(x) * -1j, t, s)

	result = ((dexp_p1 - dexp_p2) / 2j)

	if np.imag(result) == 0:
		return np.real(result)
	
	else:
		return result


"""
	The Laplace transform function.
"""
	
def laplace_transform(self, f, z, s):
	def g(t):
		return f(t) * self.dexp_p(lambda t: self.mucircleminus(z, t), self.sigma(t), s)

	return self.dintegral(g, max(self.ts), s)