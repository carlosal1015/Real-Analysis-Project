#!/opt/conda/bin/python3
# -*- coding: utf-8 -*-

"""
Suppose we want to integrate the Mackey–Glass delay differential equation: :math:`\\dot{y} = f(y)` with :math:`y∈ℝ`, 
.. math::
	f(y) = β \\frac{y(t-τ)}{1+y(t-τ)^n} - γ·y(t),
	
and with :math:`β = 0.25`, :math:`γ = 0.1`, and :math:`n = 10`.
First we do some importing and define the constants:
.. literalinclude:: ../examples/intervals.py
	:dedent: 1
	:lines: 16-18
"""

if __name__ == "__main__":
	from timescale import Timescale
