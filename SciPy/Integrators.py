
import numpy as np

def trapz(func, x, N=10):
    '''Calculates an integral using the trapezoidal method
    of the func from 0 to x, using N steps'''
    a = 0.0
    b = float(x)
    h = (b - a) / N
    
    k = np.arange(1, N)
    I = h * (0.5 * func(a) + 0.5 * func(b) + func(a + k * h).sum())
    
    return I

def simps(func, x, N=10):
    '''Calculates an integral using the simpsons method
    of the func from 0 to x, using N steps'''
    a = 0.0
    b = float(x)
    h = (b - a) / N

    k1 = np.arange(1, N / 2 + 1)
    k2 = np.arange(1, N / 2)
    I = (1./3.) * h * (func(a) + func(b) + 4.*func(a + (2 * k1 - 1) * h).sum() \
                       + 2.*func(a + 2 * k2 * h).sum())
    
    return I