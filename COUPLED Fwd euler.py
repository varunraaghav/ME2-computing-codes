# session 7, task C - 


import math 
import numpy as np
import matplotlib.pyplot as plt


### F1 and F2 are the derviatives vector

def Func1 (y1, y2, t):
    F1 = 0.3*y1*y2 - 0.8*y1
    return F1

def Func2 (y1, y2, t):
    F2 = 1.1*y2 - y1*y2      ### although Y1 and Y2 are not a function of time (t), this is a generic solution
    return F2





def FwEulerTwo(h, Y0, t0, t_end):
    n = int(t_end/h)
    t = np.arange(t0, t_end, h)
    
    Y1 = []
    Y2 = []
    
    Y1.append(Y0[0])
    Y2.append(Y0[1])
    
    
    for i in range(1, n+1):
        
         Y1.append(Y1[i-1] + (h*Func1(Y1[i-1], Y2[i-1], t[i-1])))
         Y2.append(Y2[i-1] + (h*Func2(Y1[i-1], Y2[i-1], t[i-1])))
    
    
    
    Y = np.array([Y1, Y2])
    
    return Y, t
    



t_end = 40
t0 = 0
h = 0.019
Y0 = [0.8, 7]

Y_FwSystem , t_FwSystem = FwEulerTwo(h, Y0, t0, t_end) 


# y1, y2 , t =  FwEulerTwo(h, Y0, t0, t_end) 


plt.figure(dpi = 1200)
plt.xlabel('time (t)')
plt.ylabel('y')


plt.plot(t_FwSystem, Y_FwSystem[0],  '-', color = 'blue', label = '£')
plt.plot(t_FwSystem, Y_FwSystem[1],  '-', color = 'orange', label = 'N')
plt.legend()
