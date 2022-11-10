import matplotlib.pyplot as plt
import numpy as np
import math

def func(x):
    y = 1/ (1 + 25 * x**2)
    return y
    

### solving divided diff recrsively

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
P = NewtonInterpolation(xn, yn, x)

plt.figure(dpi=800)
plt.plot(x,P, color='red', label = 'newton')
plt.scatter(xn, yn, color = 'blue', label = 'nodes')
plt.plot(x, func(x), color = 'green', label = 'actual')
plt.grid()
plt.legend()
plt.show()