# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 16:40:51 2022

@author: varun
"""

import numpy as np
import matplotlib.pyplot as plt
import math as mt

def TrBaryc(r,f,rp):
    # form matrix A
    # the first two rows of A are the x and y coordinates of the three vertices
    A = np.copy(np.transpose(r))
    # third row of A is made of ones
    A = np.append(A,[[1,1,1]], axis=0)
    # form d
    # first two rows of d are the x and y coordinate of rp, third row is a one
    d = np.append(rp,1)
    # invert A and multiply by d to find the lambdas
    l = np.dot(np.linalg.inv(A),d)
    # interpolate with the lambdas
    frp = l[0]*f[0] + l[1]*f[1] + l[2]*f[2]
    return frp

# define a triangle
r = np.array([[0,0],[1,1],[2,0]])
# define a point rp within the triangle
rp = np.array([1,0.5])
# define the value of teh function at the vertices
f = np.array([0,1,3])

# interpolate
frp = TrBaryc(r,f,rp)
print(frp)
# append rp to the vertices and frp for f
r = np.append(r,[rp],axis=0)
f = np.append(f,frp)
print(r)

# plot in 3d: f vs (x and y)
x = r[:,0]
y = r[:,1]
print(f)
fig, (ax1) = plt.subplots(nrows=1)
ax1.tricontour(x, y, f, levels=14, linewidths=0.5, colors='k')
cntr1 = ax1.tricontourf(x, y, f, levels=14, cmap="RdBu_r")
fig.colorbar(cntr1, ax=ax1)
ax1.plot(x,y,'ko', ms=3)