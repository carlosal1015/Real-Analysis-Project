from timescale import Timescale_new as tsc
from sympy import (
	Set,
	S,
	Rational,
	Lambda,
	Symbol,
	Range,
	oo
	)
from sympy.sets.sets import FiniteSet, Interval
from sympy.sets.fancysets import ImageSet

t = Symbol('t')

# Iterables

TS0 = tsc() # Emptyset.
TS1 = tsc(Range(-oo, 1 - 1, 3)) # 
TS2 = tsc(S.Naturals) # Set of naturals.
TS3 = tsc(S.Naturals0) # Set of naturals including zero.
TS4 = tsc(S.Integers) # Set of integers.
TS5 = tsc(ImageSet(Lambda(t, -t), S.Naturals))
# TODO: Rational numbers

# Non-interables

TS9 = tsc(S.Reals) #Interval(-oo,+oo)
TS10 = tsc(S.UniversalSet)

# print(list(TS1.ts))

# TODO: Implementar raise
try:
    iterator = iter(TS9.ts)
except TypeError:
	# TODO: Definir la cardinadad (números cardinales y números ordinales) del tiempo de escala.
    print("El objeto no es iterable.")
else:
	# TODO: En el caso finito, asignarle su cardinal.
    print("Es iterable.")

# https://docs.sympy.org/latest/tutorial/printing.html