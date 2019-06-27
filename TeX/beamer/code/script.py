#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 11:01:31 2019

@author: Oromion
"""
from pylab import *
import euler_01

x0 = array([0., 1.])
t = arange(0, 10, 0.01)

X = euler_01.euler(euler_01.func, x0, t)

plot(t, X)
show()