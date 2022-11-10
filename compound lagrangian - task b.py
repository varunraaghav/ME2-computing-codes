# -*- coding: utf-8 -*-
"""
Created on Fri Jun 10 02:49:49 2022

@author: varun
"""

import matplotlib.pyplot as plt
import numpy as np


################## inputting sety1 and sety2 from textfile

file = open('set1.txt', 'r')
f1 = file.readlines()
file.close()
sety1 = []

for i in range (0, len(f1)):
    sety1.append(int(f1[i].rstrip()))
    i += 1
    

file = open('set2.txt', 'r')
f2 = file.readlines()
file.close()
sety2 = []

for i in range (0, len(f2)):
    sety2.append(int(f2[i].rstrip()))
    i += 1
#############################################################
    
xn1 = np.arange(0,10+0.5,0.5)   #### xn1 index
xn2 = np.arange(0,10+0.6,0.6)   ### xn2 index

xn = np.arange(2,8+0.05,0.05)   #### xn index, as stated in question

################ Lagrangian, Lj function
def Lagrangian(j, xn, xp):
    n = len(xn)
    
    L = 1
    for k in range(0,n):
        if k!= j:
            L *= (xp - xn[k]) / (xn[j] - xn[k]) 
    
    return L

##################### Lagrangian interpolate function, with both sets of data
def LagrInterpolate(xn1, xn2, sety1, sety2, xn):
    N1 = len(xn1) - 1 ## interpolation number for set y1
    N2 = len(xn2) - 1 ### interpolation number for sety2
    
    z = np.zeros(len(xn))  #### initialising z matrix
    
    for i in range(len(xn)): ### looped through xn
        zp = 0
        for j in range(0,N1+1):
            zp += sety1[j] * Lagrangian(j,xn1,xn[i])  ### lagrangian with xn1, set y1
        
        for k in range(0,N2+1):
            zp += sety2[k] * Lagrangian(k, xn2, xn[i]) ### lagrangian with xn2, set y2
        
        z[i] = zp  ### z = y1 + y2 
        
    return z

############ plotting nodes and polynomial
plt.figure(dpi=800)
plt.plot(xn1,sety1, 'x')
plt.plot(xn2,sety2, 'o')

Z = LagrInterpolate(xn1, xn2, sety1, sety2, xn)
plt.plot(xn,Z)

