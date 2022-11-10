# session 7, task a , b: ODEs methods


import math 
import numpy as np
import matplotlib.pyplot as plt

##making function (dy/dt = ___)
def Func(y,t):
    F = -2*y*t -2*t**3
    return F




def FwEuler(t0, y0, h, t_end):
    n = int(t_end/h)
    t = np.arange(t0, t_end+h, h) # array of time values   
    
    y = []
    y.append(y0)
    
    for i in range(1,n+1):
    ## forwarld euler formula
        y.append(y[i-1] + (h*Func(y[i-1],t[i-1])))  ## note al the indexes say i-1 , we are trying to find the future y_n value in this step

    return y,t
    

    
    
## initial and boundary conditions given in the problem
t0 = 0
y0 = 100
h = 0.1
t_end = 1


y_forwEul , t_forwEul = FwEuler(t0, y0, h, t_end)

###############################################################################################################
### RK4 code 

def RK4(t0,y0,h,t_end):
    n = int(t_end/h)
    t = np.arange(t0, t_end+h, h) # array of time values   
    
    y = []
    y.append(y0)
    
    for i in range(1,n+1):
        
        k1 = h*Func( y[i-1]  ,            t[i-1])
        k2 = h*Func( y[i-1]+(0.5*k1)   ,  t[i-1]+(0.5*h) )
        k3 = h*Func( y[i-1]+(0.5*k2)   ,  t[i-1]+(0.5*h) )
        k4 = h*Func( y[i-1]+k3         ,  t[i-1]+h)
        
        y.append(y[i-1] + (k1 + 2*k2 + 2*k3 + k4)/6)
        
        
    return y,t

    
y_RK4,t_RK4 = RK4(t0,y0,h,t_end)







#################################################################################################
### Backward Euler code


def BackYn (y,t,h):
    F = (y - (2*h*t**3)) / (1+2*h*t)
    return F


def BwEuler(t0, y0, h, t_end):
    n = int(t_end/h) + 1
    t = np.arange(t0, t_end+h, h) # array of time values   
    
    y = np.ndarray(n)
    y[0] = y0
    
    for i in range(1,n):
    ## Backward euler formula
        y[i] = (BackYn(y[i-1], t[i] , h))

    return y,t


y_backEul ,t_backEul = BwEuler(t0, y0, h, t_end)
    


plt.figure(dpi = 1200)
plt.xlabel('time (t)')
plt.ylabel('y')

plt.plot(t_forwEul, y_forwEul, '.', color = 'blue', label = 'Forward Euler')
plt.plot(t_backEul, y_backEul, '.', color = 'green', label = 'Backward Euler')
plt.plot(t_RK4, y_RK4, '.', color = 'red', label = 'RK4')

plt.legend()
plt.grid(linestyle = '--')








