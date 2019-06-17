from timescale.classes.timescale import Timescale
from scipy.misc import derivative

"""
	Función delta derivada
"""
def dderivative(self,f,t):
	if self.sigma(t) == t:
		return derivative(f, t, dx=(1.0/2**16))

	else:
		return (f(self.sigma(t))-f(t))/self.mu(t)


"""
	Función nabla derivada
"""
def nderivative(self,f,t):
	return (f(t)-f(self.rho(t)))/self.nu(t)