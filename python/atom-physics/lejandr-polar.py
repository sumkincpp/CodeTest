# -*- coding: cp1251 -*-
'''import matplotlib
import numpy as np
from matplotlib.pyplot import figure, show, rc, gridalf', 'Full'])'''

from pylab import *

#Classic KOII, Lejandr Polynom
def P(x, l, m = 0):
    if m == 0:
        if l == 0:
            return 1
        elif l == 1:
            return x
    
    m = 0
    
    #return (2*l-1)/(l-m)*x*P(x, l-1, m)-(l-1+m)/(l-m)*P(x, l-2, m)
    return (2*l-1)*x*P(x, l-1, m)/(l-m)-(l-1+m)*P(x, l-2, m)/(l-m)
	
close('all')


width, height = matplotlib.rcParams['figure.figsize']
size = min(width, height)-2
print size
# make a square figure
fig = figure(figsize=(size, size))
plt = fig.add_axes([0.1, 0.1, 0.8, 0.8], polar=True)

theta = arange (0, 2*pi, 0.3)
theta2 = arange (0, 2*pi, 0.01)

#polar (theta, cos(theta))

some = ['+', 'o', 's', 'x']

for i in range(1, 5):
    print i, P(2, i)
    
    plt.plot (theta2, P(cos(theta2), i))
    plt.plot (theta, P(cos(theta), i), some[i-1],  label=r'$P_{%s}(cos(\theta))$' % i)
    #polar (theta, P(cos(theta), i), label='$P_{%s}(cos(%sheta))$' % i, 'F')

rval = [j/4 for j in range(5)];

rgrids([0.5, 1.0, 1.5, 2.0])

dy = 0

sp_ax = plt.get_position()
print sp_ax
plt.set_position([sp_ax.x0, sp_ax.y0+dy,
sp_ax.x1-sp_ax.x0, sp_ax.y1-sp_ax.y0])



#theta_labels = ['0', r'$\frac{\pi}{2}$', r'$\pi$', r'$\frac{3*\pi}{2}$']
#thetagrids(arange(0, 360, 90), theta_labels)

legend(loc='lower right');
title(r'Polar Legendre polynomials')
show()

'''
import numpy as npd

def PI(): return 3.1415;

def fact(x):
    if x == 0:
        return 1;

    return x*fact(x-1)

def H_0(x):
    return 1

def H_1(x):z
    return x

def H(x, n):
    
    if n == 1:
        return H_1(x)
    if n == 0:
        return x-x+1

    return 2*x*H(x, n-1) - 2*(n-1)*H(x, n-2)

def psi_n(x, n):
    Cn = 1/(2**n*fact(n)*x*sqrt(pi))
    
    return e**(-1/2*x*x)*H(x, n);

t1 = np.arange(-5.0, 5.0, 0.01)

plt.figure(1)

for j in range(0,5):
    print j
    
    plt.plot(t1, H(t1, j), label='$H_%s(x)$' % j)

    #plt.plot(t1, psi_n(t1, j), label='$\psi_{%s}$' % j)

    #plt.plot(t1, psi_n(t1, j)*psi_n(t1, j), label='$\psi_{%s}^2$' % j)


plt.legend()
#plt.grid(color='b', linestyle='-', linewidth=0.5);
plt.axhline(0, -5, 5)
plt.axvline(0, -15, 15)
plt.axis([-5, 5, -15, 15])
#plt.axis([-3, 3, -4, 14])
#plt.axis([-3, 3, -4, 20])'''
#plt.savefig("some.png")
