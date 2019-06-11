#!/usr/bin/python
# -*- coding: utf8 -*-
from math import log as ln

def present_amount(A0, p, n):
	return A0*(1 + p/(360.0*100))**n


def initial_amount(A, p, n):
	return A*(1 + p/(360.0*100))**(-n)


def annual_rate(A0, A, n):
	return 360*100*((A/A0)**(1.0/n) - 1)


def days(A0, p, n):
	return ln(A/A0)/ln(1 + )

if __name__ == "__main__":
	import sys
	p = float(sys.argv[1])
	years = days(1, 2, p)/365.0
	print("With p = {:2} it takes {:2} years to double".format(p, years))