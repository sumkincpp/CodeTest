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
    
    #return (2*l-1)/(l-m)*x*P(x, l-1, m)-(l-1+m)/(l-m)*P(x, l-2, m)
    return (2*l-1)*x*P(x, l-1, m)/(l-m)-(l-1+m)*P(x, l-2, m)/(l-m)
	
close('all')

theta = arange (0, 2*pi, 0.3)
theta2 = arange (0, 2*pi, 0.01)

some = ['+', 'o', 's', 'x', 'D', '^']

for i in range(1, 6):
    plt.plot (theta2, P(cos(theta2), i))
    plt.plot (theta, P(cos(theta), i), some[i-1],  label=r'$P_{%s}(cos(\theta))$' % i )

plt.axis([0, 2*pi, -3, 3])
plt.grid()
plt.ylabel(r'$P_{n}(cos(\theta))$')
plt.xlabel(r'angle, $\theta$')
plt.xticks([0, pi/2, pi, 3*pi/2, 2*pi], ['0', '$\pi/2$', '$\pi$', '$3*\pi/2$', '$2*\pi$'])
title('Legendre polynomials')
legend(loc='lower right')
show()
