import math
import numpy as np
import matplotlib.pyplot as plt

f = open('xn.txt', 'r')
xn = f.readlines()
xn_list = []
for i in xn:
    xn_list += [float(i.rstrip())]
f.close()
    

f = open('xs.txt', 'r')
xs = f.readlines()
xs_list = []
for i in xs:
    xs_list += [float(i.rstrip())]
f.close()    
        

f = open('yn.txt', 'r')
yn = f.readlines()
yn_list = []
for i in yn:
    yn_list += [float(i.rstrip())]
f.close()


f = open('ys.txt', 'r')
ys = f.readlines()
ys_list = []
for i in ys:
    ys_list += [float(i.rstrip())]
f.close()


def trapz(x,y):
    N = len(x)-1
    I = 0

    for n in range(0,N):
        h = x[n+1] - x[n]
        I += 0.5 * (y[n+1]+y[n]) * h
        
    return I

plt.figure(dpi=1200)
plt.plot(xn_list,yn_list,'-', color='lightblue')
plt.plot(xs_list,ys_list,'-', color='lightblue')
plt.axis('equal')  


I_north = trapz(xn_list,yn_list)
print(I_north)
I_south = trapz(xs_list, ys_list)
print(I_south)

I_middle = I_north - I_south
print('Surface area of river is ' , I_middle)


