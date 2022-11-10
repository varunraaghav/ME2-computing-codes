import numpy as np
import matplotlib.pyplot as plt

def f(x):
    y = 1/np.sqrt(x**18.10+2021)
    #y = np.sin(x)
    return y
# lower boundary
a = 0
# upper boundary
b = 2
# number of equidistant nodes
N = 10

x = np.linspace(a,b,N) # remember, with linespace we have to provide the number of nodes and not intervals
print(x)
# compute points for f(x) at nodes x
y = f(x)



# Task C
# function trapz: compute numerical integration with trapezium rule, for nodes at any distance
def trapz(x,y):
    # get the number of subintervals
    N = len(x) - 1
    # compute the integral
    # set range for the trapezia: there are as many trapezia as the number of intervals
    R = range(0,N)
    S = 0
    for i in R:
        # compute the area of this single trapezium (remind yourself the area of a trapezium)
        S += 0.5 * (y[i+1] + y[i]) * (x[i+1] - x[i])
    return S

# test with one of the previous functions
I = trapz(x,y)
print(I)