import matplotlib.pyplot as plt
import numpy as np
import math

def func(x):
    y = np.sin(x)
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


def NewtonDivDiff(xn,yn):
    N = len(xn) -1
    
    if N == 0:
        f = yn[0]
        
    else:
        f =( NewtonDivDiff(xn[:-1],yn[:-1] - NewtonDivDiff(xn[1:],yn[1:])) / (xn[0] - xn[-1]))
        
    return f


def NewtonInterpolation(xn,yn,x):
    k = len(xn) -1
    y = []
    
    for xp in x:
        yp = yn[0]
        
        for i in range(1,k+1):
            product = 1
            for j in range(0,i):
                product *= (xp - xn[j])
                
            yp += product * NewtonDivDiff(xn[0:i+1],yn[0:i+1])
            
        y += [yp]
        
    y = np.array(y)  ### convert list to array
    
    return y

a = 1
b = 2
N = 4  ## type of interpolation
xn = np.linspace(a,b,N)

yn = func(xn)

x = np.linspace(0,3,50)
P = LagrInterpolate(xn, yn, x)
P2 = NewtonInterpolation(xn, yn, x)

plt.figure(dpi=800)
plt.plot(x,P, color='red', label = 'lagrangian')
plt.plot(x,P2, color='orange', label = 'Newton')
plt.scatter(xn, yn, color = 'blue', label = 'nodes')
plt.plot(x, func(x), color = 'green', label = 'actual')
plt.grid()
plt.legend()
plt.show()






            
    