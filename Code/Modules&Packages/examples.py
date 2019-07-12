from timescale import Timescale as tsc
from sympy import (
	Interval,
	Rational,
	nsimplify,
	symbols,
	pi,
	sqrt,
	S,
	oo,
	assumptions,
	Q,
	ask,
	var,
	sin,
	Lambda
 )
from sympy.sets.fancysets import ImageSet


TS1 = tsc(Rational(".1"), 'documentation example')

a = Rational(".1")
b = S("8/9")
I = Interval(a, b)
t = symbols('t', nonnegative=True)
z = var('z', real=True)

#print(c.limit_denominator(10**13))
#a, b, c = symbols('a b c')
#x = nsimplify(sqrt(pi)*(0.333333333333333*a + 0.333333333333333*b - #2.66666666666667*c**2))

T = Interval(-oo, +oo).interior

Reals = S.Reals#Interval(-oo,+oo)
#Rationals = 
#Irrationals = Complement(Reals, Rationals)
Integers = S.Integers

Naturals = S.Naturals

#print(sqrt(-1) in Reals)
Negatives = ImageSet(Lambda(t, -t), Naturals)
print(-pi in Negatives)
sigma = T.inf
#rho = T1.sup

#Q.is(True) = True

#print(ask(Q.extended_real(oo)))
#print(t.assumptions0)

#print(f(t) in Interval(0, 1))
#print(f(t) in Interval(0,1))

#print("El intervalo I es cerrado?",I.is_closed)

#print("0 está en en el intervalo I?",0 in I)