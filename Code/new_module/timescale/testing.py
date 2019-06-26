from timescale import Timescale
from definitions import (
	sigma,
	rho,
	mu,
	nu,
	integers,
	quantum,
)
from differenciation import (
	dderivative,
	nderivative,
)

Timescale1 = Timescale([0, 1, 2, 3, 4, 5, 6, 7], 'documentation example')

print(Timescale1.ts)

print(sigma(Timescale1, 2))


print(dderivative(Timescale1, 2, 0.1))
