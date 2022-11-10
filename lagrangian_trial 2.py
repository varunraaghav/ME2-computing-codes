import matplotlib.pyplot as plt
import numpy as np
import math

def func(x):
    y = np.cos(x)
    return y


def Lagrangian(j, xn, xp):
    n = len(xn)
    
    L = 1
    for k in range(0,n):
        if k!= j:
            L *= (xp - xn[k]) / (xn[j] - xn[k])
            
    
    return L


def LagrInterpolate(xn, yn, x):
    N = len(xn) - 1 ## interpolation number
    
    y = np.zeros(len(x))
    
    for i in range(len(x)):
        yp = 0
        for j in range(0,N+1):
            yp += yn[j] * Lagrangian(j,xn,x[i])
                
        y[i] = yp
        
    return y

a = 1
b = 2
N = 4  ## type of interpolation
xn = np.linspace(a,b,N)

yn = func(xn)

x = np.linspace(0,3,50)
P = LagrInterpolate(xn, yn, x)

plt.figure(dpi=800)
plt.plot(x,P, color='red', label = 'lagrangian')
plt.scatter(xn, yn, color = 'blue', label = 'nodes')
plt.plot(x, func(x), color = 'green', label = 'actual')
plt.grid()
plt.legend()
plt.show()






            
    