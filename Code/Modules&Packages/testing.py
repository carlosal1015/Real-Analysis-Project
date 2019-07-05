from timescale.timescale import Timescale_new as tsc

from sympy import (
	Set,
	S,
	Rational,
	Lambda,
	Symbol,
	Range,
	oo,
	Interval,
	latex
	)
from sympy.sets.sets import FiniteSet, Interval
from sympy.sets.fancysets import ImageSet

t = Symbol('t')
T = Symbol(r'\mathbb{T}')
# Iterables
print(latex(T))
TS0 = tsc(S.EmptySet, latex(T) + '=' + latex(S.EmptySet))
TS1 = tsc(Range(-2, 1), latex(T) + '=' + latex(Range(-2, 1)))
TS2 = tsc(Range(-oo, 5, 5), latex(T) + '=' + latex(Range(-oo, 5, 5)))
TS3 = tsc(Range(0, oo, 7), latex(T) + '=' + latex(Range(0, oo, 7)))
TS4 = tsc(S.Naturals, latex(T) + '=' + latex(S.Naturals))
TS5 = tsc(S.Naturals0, latex(T) + '=' + latex(S.Naturals0))
TS6 = tsc(S.Integers, latex(T) + '=' + latex(S.Integers))
TS7 = tsc(ImageSet(Lambda(t, -t), S.Naturals), latex(T) + '=' + latex(ImageSet(Lambda(t, -t), S.Naturals)))
# TODO: Create an instance of rational numbers in some subset like Interval(0,1s).
# TODO: Recorrer las fracciones de la siguiente manera:
# https://mathoverflow.net/questions/200656/is-there-a-natural-bijection-from-mathbbn-to-mathbbq

# Non-interables

TS9 = tsc(S.Reals, latex(T) + '=' + latex(S.Reals)) # Means Interval(-oo,+oo).
TS10 = tsc(S.UniversalSet, latex(T) + '=' + latex(S.UniversalSet))
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

print(S.Reals.is_closed)

print(TS0.__dict__)

#TSX = input("Ingrese la escala de tiempo: ")
#locals()[TSX] = tsc()
#print(X.boundary)
# https://docs.sympy.org/latest/tutorial/printing.html