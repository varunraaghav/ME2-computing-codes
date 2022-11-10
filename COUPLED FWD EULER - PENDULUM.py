# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 16:47:57 2022

@author: varun
"""

# session 7, task D - 


import math 
import numpy as np
import matplotlib.pyplot as plt


### F1 and F2 are the derviatives vector

def Func1 (y1, y2, t):
    F1 = y2
    return F1

def Func2 (y1, y2, t):
    c = 0.05
    L = 1
    m = 0.5
    g = 9.81
    
    F2 = (-c/m)*y2 -(g/L)*np.sin(y1)
    ### although Y1 and Y2 are not a function of time (t), this is a generic solution
    return F2





def FwEulerTwo(h, Y0, t0, t_end):
    n = int(t_end/h)
    t = np.arange(t0, t_end+h, h)
    
    Y1 = []
    Y2 = []
    
    Y1.append(Y0[0])
    Y2.append(Y0[1])
    
    
    for i in range(1, n+1):
        
         Y1.append(Y1[i-1] + (h*Func1(Y1[i-1], Y2[i-1], t[i-1])))
         Y2.append(Y2[i-1] + (h*Func2(Y1[i-1], Y2[i-1], t[i-1])))
    
    
    
    Y = np.array([Y1, Y2])
    
    return Y, t
    



t_end = 15
t0 = 0
h = 0.002
Y0 = np.zeros(2)
Y0[0] = np.pi/4  ## initial angular displacement
Y0[1] = 0 ### initial velocity of system = 0

Y_FwSystem , t_FwSystem = FwEulerTwo(h, Y0, t0, t_end) 


# y1, y2 , t =  FwEulerTwo(h, Y0, t0, t_end) 


plt.figure(dpi = 1200)
plt.xlabel('time (t)')
plt.ylabel('y')


plt.plot(t_FwSystem, Y_FwSystem[0],  '-', color = 'blue', label = 'displacement')
plt.plot(t_FwSystem, Y_FwSystem[1],  '-', color = 'orange', label = 'time')
plt.legend()


