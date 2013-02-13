import numpy as np
import matplotlib.pyplot as plt
from math import sqrt, pi, e

def PI(): return 3.1415;

def fact(x):
    if x == 0:
        return 1;

    return x*fact(x-1)

def H_0(x):
    return 1

def H_1(x):
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
#plt.axis([-3, 3, -4, 20])
plt.savefig("some.png")
