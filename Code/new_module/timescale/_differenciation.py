#!/opt/conda/bin/python3
# -*- coding: utf-8 -*-

#from timescale.timescale import Timescale
#from timescale.definitions import sigma, mu
from scipy.misc import derivative

def dderivative(self, f, t):
	"""
	Función delta derivada
	"""
	if self.sigma(t) == t:
		return derivative(f, t, dx=(1.0/2**16))

	else:
		return (f(self.sigma(t))-f(t))/self.mu(t)


def nderivative(self, f, t):
	"""
	Función nabla derivada
	"""
	return (f(t)-f(self.rho(t)))/self.nu(t)
