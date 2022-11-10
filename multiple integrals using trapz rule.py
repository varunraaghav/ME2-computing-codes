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



    
    



# Task E (optional)


R = 5 # set radius of the domain

# set the step intervals in x and y
dx = 0.05
dy = 0.05

# set the x range, not including the boundaries
x = np.arange(-R+dx,R,dx)
N = len(x)
# the y range depends of the various values of x, and cannot be fixed here

# integrate in dy, for all the value of x, i.e. find G(x)

G = np.zeros(N)
# for every x
for i in range(0,N):
    # determine the boundaries m and p for this x
    mx = np.sqrt(R**2-x[i]**2)
    px = mx
    # set the y points for this x, not including the boundaries
    y = np.arange(-mx+dy,px,dy)
    z = np.zeros(len(y))
    # determine the values of the function z(x,y)
    for j in range(0,len(y)):
        z[j] = np.sqrt(R-np.sqrt(x[i]**2+y[j]**2)) # dome of Samarkand
        # z[j] = np.sqrt(R**2-x[i]**2-y[j]**2) # emisphere
    
    # integrate in dy from cx to dx (for this specific x)
    G[i] = trapzeqd(y,z) # G(x)

# integrate G(x) in dx
I = trapzeqd(x,G)

print(I)


import matplotlib.pyplot as pl
from mpl_toolkits import mplot3d

# plot the dome

# set domain in polar coordinates
r = np.linspace(0,R,100)
t = np.linspace(0,2*np.pi,100)
# set 2D mesh grids
[Rg, Tg] = np.meshgrid(r,t)

# calculate X and Y (2D meshgrids)
X = Rg*np.cos(Tg)
Y = Rg*np.sin(Tg)

# calculate Z(X,Y)
Z = np.sqrt(R-np.sqrt(X**2+Y**2))

# plost as surface
ax = pl.axes(projection='3d')
ax.plot_surface(X,Y,Z)