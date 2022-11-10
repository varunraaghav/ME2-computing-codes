import math
import numpy as np
import matplotlib.pyplot as plt


def f(x):
    y = 1/np.sqrt((x**18.1) + 2021)
    return y



def trapzeqd(x, y):
    N = len(x) - 1
    h = x[1]-x[0]
    S = 0
    
    I = 0
    I += y[0]/2 + y[-1]/2
    
    for n in range(1, N):
        S += y[n]

    I += S
    I = I*h

    print(I)  
    return I      
    
plt.figure(dpi=1200)

    
for i in range (1, 5):
    b = 10**i
        
    x = np.linspace(0,b,5)
    y = f(x)
    
    I = trapzeqd(x,y)
    
    plt.plot(b,I,'x')    



    
    

