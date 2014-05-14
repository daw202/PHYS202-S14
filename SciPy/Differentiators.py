
import numpy as np

def twoPtForwardDiff(x, y):
    '''
    Takes two arrays x and y of the same shape and calculates the
    forward differential of the second with respect to the first. 
    In the case of the last data point it uses a backwards differentiation 
    instead of a forwards differentiation because there is no next 
    point in the forward direction.
    '''
    dydx = np.zeros(y.shape, float)
    dydx[0:-1] = np.diff(y)/np.diff(x)
    dydx[-1] = (y[-1] - y[-2])/(x[-1] - x[-2])
    return dydx

def twoPtCenteredDiff(x, y):
    '''
    Takes two arrays x and y of the same shape and calculates the
    center differential of the second array with respect to the first.
    For the first and last data point it uses a forward differential
    and backward differential respectively because the endpoints don't
    have points on both sides
    '''
    dydx = np.zeros(y.shape, float)
    dydx[1:-1] = (y[2:] - y[:-2])/(x[2:] - x[:-2])
    dydx[0] = (y[1] - y[0])/(x[1] - x[0])
    dydx[-1] = (y[-1] - y[-2])/(x[-1] - x[-2])
    return dydx

def fourPtCenteredDiff(x, y):
    '''
    Takes two arrays x and y of the same shape and calculates the
    center differential of the second array with respect to the first.
    For the first and last data point it uses a forward differential
    and backward differential respectively because the endpoints don't
    have points on both sides
    '''
    dydx = np.zeros(y.shape, float)
    dydx[2:-2] = (y[:-4] - 8*y[1:-3] + 8*y[3:-1] - y[4:]) / \
                    (x[:-4] - 8*x[1:-3] + 8*x[3:-1] - x[4:])
    
    dydx[1] = (y[2] - y[0])/(x[2] - x[0])
    dydx[-2] = (y[-1] - y[-3])/(x[-1] - x[-3])
    dydx[0] = (y[1] - y[0])/(x[1] - x[0])
    dydx[-1] = (y[-1] - y[-2])/(x[-1] - x[-2])
    return dydx