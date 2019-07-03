import numpy as np
import matplotlib.pyplot as plt
from mpmath import *
from pylab import rcParams

rcParams['figure.figsize'] = 10, 10

x=np.arange(-15,20,1);

def integerexp(a,t,s):
	return (1+a)**(t-s)

def returnzero(t):
	return 0

def integercosine(t): # a=0.6,s=0
	return (integerexp(0.6j,t,0)+integerexp(-0.6j,t,0))/2

f=np.vectorize(lambda x : integercosine(x).real)
y=f(x)

def g(x):
	return 0

h=np.vectorize(g)
y2=h(x)

fig, ax = plt.subplots()

plt.xlabel(r'$t$')
plt.ylabel(r'$\cos_{0.6}(t,0;\mathbb{Z})$')
plt.title(r'Time scale delta cosine function')

plt.scatter(x,y,color='Black',s=40)
plt.plot(x,y2,'--',linewidth=2,color='Black')

plt.xlim([-15,20])
plt.savefig('integerdeltacosine,a=0.6,s=0plot.png',bbox_inches='tight',pad_inches=0.15)