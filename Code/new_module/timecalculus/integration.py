import numpy as np

def dintegral(self,f,t,s):
	"""
	delta integral
	"""
	# The following code checks that t and s are elements of the timescale

	tIsAnElement = False
	sIsAnElement = False

	for x in self.ts:
		if not isinstance(x, list) and x == t:
			tIsAnElement = True

		if not isinstance(x, list) and x == s:
			sIsAnElement = True

		if isinstance(x, list) and  (t >= x[0] and t <= x[1]):
			tIsAnElement = True

		if isinstance(x, list) and  (s >= x[0] and s <= x[1]):
			sIsAnElement = True

		if tIsAnElement and sIsAnElement:
			break

	if not tIsAnElement and not sIsAnElement:
		raise Exception("The bounds of the dintegral function, t and s, are not elements of the timescale.")

	elif not tIsAnElement:
		raise Exception("The upper bound of dintegral function, t, is not an element of timescale.")

	elif not sIsAnElement:
		raise Exception("The lower bound of dintegral function, s, is not an element of timescale.")

	# Validation code ends

	points = []
	intervals = []

	for x in self.ts:
		if not isinstance(x, list) and s <= x and t > x:
			points.append(x)

		elif isinstance(x, list) and s <= x[0] and t > x[1]:
			points.append(x[1])
			intervals.append(x)

		elif isinstance(x, list) and s <= x[0] and t == x[1]:
			intervals.append(x)

		elif isinstance(x, list) and (s >= x[0] and s <= x[1]) and (t > x[1]):
			points.append(x[1])
			intervals.append([s, x[1]])

		elif isinstance(x, list) and (s >= x[0] and s <= x[1]) and (t == x[1]):
			intervals.append([s, x[1]])

		elif isinstance(x, list) and (s >= x[0] and s < x[1]) and (t < x[1]):
			intervals.append([s, t])

		elif isinstance(x, list) and (s < x[0]) and (t >= x[0] and t < x[1]):
			intervals.append([x[0], t])

	sumOfIntegratedPoints = sum([self.mu(x)*f(x) for x in points])

	# sumOfIntegratedIntervals = sum([integrate.quad(f, x[0], x[1])[0] for x in intervals])
	
	sumOfIntegratedIntervals = sum([self.integrate_complex(f, x[0], x[1]) for x in intervals])

	return sum([sumOfIntegratedPoints, sumOfIntegratedIntervals])


# Utility function to integrate potentially complex functions.

def integrate_complex(self, f, s, t, **kwargs):
	def real_component(t):
		return np.real(f(t))
		
	def imaginary_component(t):
		return np.imag(f(t))
	
	real_result = integrate.quad(real_component, s, t, **kwargs)[0]
	
	imaginary_result = integrate.quad(imaginary_component, s, t, **kwargs)[0]
	
	if imaginary_result == 0:
		return real_result
	
	else:        
		return real_result + 1j*imaginary_result


def g_k(self, k, t, s):
	"""
	Generalized g_k polynomial from page 38 with memoization.
	"""
	if (k < 0):
		raise Exception("g_k(): k should never be less than 0!")

	elif (k != 0):
		currentKey = str(k) + ":" + str(t) + ":" + str(s)

		if currentKey in self.memo_g_k:
			return self.memo_g_k[currentKey]

		else:
			def g(x):
				return self.g_k(k - 1, self.sigma(x), s)

			integralResult = self.dintegral(g, t, s)

			self.memo_g_k[currentKey] = integralResult

			return integralResult

	elif (k == 0):
		return 1


def h_k(self, k, t, s):
	"""
	Generalized h_k polynomial from page 38 with memoization.
	"""
	if (k < 0):
		raise Exception("h_k(): k should never be less than 0!")

	elif (k != 0):
		currentKey = str(k) + ":" + str(t) + ":" + str(s)

		if currentKey in self.memo_h_k:
			return self.memo_h_k[currentKey]

		else:
			def h(x):
				return self.h_k(k - 1, x, s)

			integralResult = self.dintegral(h, t, s)

			self.memo_h_k[currentKey] = integralResult

			return integralResult

	elif (k == 0):
		return 1