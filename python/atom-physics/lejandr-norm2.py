# -*- coding: cp1251 -*-
'''import matplotlib
import numpy as np
from matplotlib.pyplot import figure, show, rc, gridalf', 'Full'])'''

from pylab import *

#Classic KOII, Lejandr Polynom
def Pl(x, l, m = 0):

    if l == 0:
        return 1+x-x
    elif l == 1:
        return x
    
    m = 0
    return (2*l-1)*x*Pl(x, l-1, m)/(l-m)-(l-1+m)*Pl(x, l-2, m)/(l-m)

close('all')

x = arange (-1, 1, 0.3)
x2 = arange (-1, 1, 0.01)

some = ['+', 'o', 's', 'x', 'D', '^']

for i in range(0, 6):
    print i
    plt.plot (x2, Pl(x2, i))
    plt.plot (x, Pl(x, i), some[i-1],  label=r'$P_{%s}(x)$' % i )

plt.axis([-1, 1, -1, 2])
plt.grid()
plt.ylabel(r'$P_{n}(x)$')
plt.xlabel(r'$x$')
#plt.xticks([0, pi/2, pi, 3*pi/2, 2*pi], ['0', '$\pi/2$', '$\pi$', '$3*\pi/2$', '$2*\pi$'])
title('Legendre polynomials')
legend(loc='lower right')
show()
