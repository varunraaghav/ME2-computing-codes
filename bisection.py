import matplotlib.pyplot as plt
import numpy as np
import math
import random

# X = np.linspace(0,100,101)
# Y = np.arange(0,101,1)
# print(X)
# print(Y)


# f(x) = x^2 + -2x + +1



def func(x):
    y = x**2 + (x-2)**3 - 4
    return y

def mybisection(x1,x2,err):
    count = 0
    while abs(x1-x2) > err:
        count+=1
        x_mid = (x1 + x2) / 2
        f = func(x1) * func(x_mid)

        if f < 0:
            x2 = x_mid
        else:
            x1 = x_mid
            
            
    root = 0.5*(x1 + x2)
    
    return root, count


x1 = -10
x2 = 10
err = 0.1

print(mybisection(x1, x2, err))


###############