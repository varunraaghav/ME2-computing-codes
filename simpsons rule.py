# session 6, task a


import math 
import numpy as np
import matplotlib.pyplot as plt



def Simpson (x, y):
    N = len(y)
    I = 0
    h = x[1] - x[0]
    for i in range(0, N-2, 2): ## looping every 2 points
        I += h/3 * (y[i] + 4*y[i+1] + y[i+2])
        
    return I



n = 1
def f2(n):
    h = 0.1/n
    x = np.linspace(0, math.pi, 100*n)
    y = np.sin(x)
    
    return x, y


x , y = f2(n)


### Simpson rule with adaptive integration  

## assign fake tolerance

tolerance = 0.00001
error = tolerance * 10
S_full = Simpson(x, y)


# print(S_full)
b = 0
while error >= tolerance:
    # print(S_full)
    # h_old = h.copy()
    
    n += 1
    x, y = f2(n)
    
    S_half = Simpson(x, y)
    # print(S_half)
   
    
    error = 1/15 * (S_half - S_full)
    S_full = S_half
    
    b  += 1

print(error, b, S_full)
    