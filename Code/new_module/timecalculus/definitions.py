def sigma(self, t):
	"""
	Función Salto hacia adelante:
	\sigma(t) = \inf \{z\in\mathds{T} : z>t \}
	"""
	tIndex = 0
	tNext = None
	iterations = 0

	for x in self.ts:
		if (not isinstance(x, list) and t == x) or (isinstance(x, list) and t >= x[0] and t <= x[1]):
			tIndex = iterations
			break

		iterations = iterations + 1

	if (tIndex + 1) == len(self.ts):
		return t

	elif isinstance(self.ts[tIndex], list):
		if (t != self.ts[tIndex][1]):
			return t

		else:
			if (isinstance(self.ts[tIndex + 1], list)):
				return self.ts[tIndex + 1][0]

			else:
				return self.ts[tIndex + 1]

	else:
		tNext = self.ts[tIndex + 1]

		if isinstance(tNext, list):
			return tNext[0]

		else:
			return tNext


def rho(self,t):
	"""
	Función Salto hacia atrás:
	\rho(t) = \sup \{ z\in\mathds{T} : z<t \}
	"""
	if t==min(self.ts):
		return t
	else:
		return max([x for x in self.ts if x<t])


def mu(self,t):
	"""
	Función de granicidad:	
	\mu(t) = \sigma(t) - t
	"""
	for x in self.ts:
		if isinstance(x, list) and t >= x[0] and t < x[1]:
			return 0

		return self.sigma(t)-t


def nu(self,t):
	"""
	Función de granicidad minimal:
	\mu_{\ast} = \inf_{\tau\in\left[s,\infty\right)\cap\mathds{T}}\mu(t).
	"""
	return t-self.rho(t)


def integers(a,b):
	"""
	Create the time scale of integers {x : a <= x <= b}
	"""
	return Timescale(list(range(a,b+1)),'integers from '+str(a)+' to '+str(b))


def quantum(q,m,n):
	"""
	Create the time scale of quantum numbers of form {q^k:k=m,m+1,...,n}
	only does q^(X) where X={0,1,2,3,...} at the moment
	"""
	return Timescale([q**k for k in range(m,n)], 'quantum numbers '+str(q)+'^'+str(m)+' to '+str(q)+'^'+str(n))