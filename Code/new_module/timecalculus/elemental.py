from timescale import Timescale
from integration import *
import numpy as np

def cyl(self, t, z):
	"""
	Cylinder transformation from definition 2.21
	"""
	if (self.mu(t) == 0):
		return z
	
	else:
		return 1/self.mu(t) * np.log(1 + z*self.mu(t))


def dexp_p(self, p, t, s):
	"""
	Delta exponential based on definition 2.30
	"""
	def f(t):
		return self.cyl(t, p(t))

	return np.exp(self.dintegral(f, t, s))


def mucircleminus(self,f,t):
	"""
	forward circle minus
	"""
	return -f(t)/(1+f(t)*self.mu(t))


def dcos_p(self, p, t, s):
	"""
	The forward-derivative cosine trigonometric function.
	"""
	dexp_p1 = self.dexp_p(lambda x: p(x) * 1j, t, s)

	dexp_p2 = self.dexp_p(lambda x: p(x) * -1j, t, s)

	result = ((dexp_p1 + dexp_p2) / 2)
	
	if np.imag(result) == 0:
		return np.real(result)
	
	else:
		return result


def dsin_p(self, p, t, s):
	"""
	The forward-derivative sine trigonometric function.
	"""
	dexp_p1 = self.dexp_p(lambda x: p(x) * 1j, t, s)

	dexp_p2 = self.dexp_p(lambda x: p(x) * -1j, t, s)

	result = ((dexp_p1 - dexp_p2) / 2j)

	if np.imag(result) == 0:
		return np.real(result)
	
	else:
		return result

	
def laplace_transform(self, f, z, s):
	"""
	The Laplace transform function.
	"""
	def g(t):
		return f(t) * self.dexp_p(lambda t: self.mucircleminus(z, t), self.sigma(t), s)

	return self.dintegral(g, max(self.ts), s)