import matplotlib.pyplot as plt
import numpy as np
import math

def func(x):
    y = 1/ (1 + 25 * x**2)
    # y = np.sin(x)
    return y



######## MyGauss Function

def MyGauss(A,b):
    
    # number of equations
    n = len(b)
    
    # eliminate the unknowns, from first to (n-1)th unknown, to form an upper triangular matrix
    for i in range(0,n-1):
        # eliminate the i-th unknown from the (i+1)th row downwards
        # i.e. set the zeros in column i.
        for j in range(i+1,n):
            # eliminate on row j

            # A(i,i) is the pivot coefficient
            p = A[j,i] / A[i,i]
        
            # compute the new elements of row j in matrix A
            # use slicing
            #A[j,:] = A[j,:] - p * A[i,:]
            # or, alternatively, loop for every cell of row j
            #for k in range(i,n):
            #    A[j,k] = A[j,k] - p * A[i,k]
            A[j,:] = A[j,:] - p * A[i,:]

            # compute the new element of row j in vector b
            b[j] = b[j] - p * b[i]
    
    
    # evauate, by back substitution the solution
    # start from the last unknown and go upward till the first unknown
    x = np.zeros(n)
    for i in range(n-1,-1,-1):
        # contribution from b (right hand side of the equation)
        x[i] = b[i] / A[i,i]
        # contribution from the other (already evaluated) unknowns
        # (within the left hand side of the equation)
        for k in range(i+1,n):
            x[i] = x[i] - A[i,k] * x[k] / A[i,i]

    return x

######################################################################


## Cubic splines:
    

def spline(xn, yn, bc_lower, bc_upper, x):
    N = len(xn) - 1
    y = np.zeros(len(x))

    aj = np.zeros(N)
    bj = np.zeros(N)
    cj = np.zeros(N)
    dj = np.zeros(N)
    
    A = np.zeros((N+1,N+1))
    b = np.zeros(N+1)
    
    A[0,0] = 1
    b[0] = bc_lower
    A[-1,-1] = 1
    b[-1] = bc_upper
    
    for j in range(1,N):
        A[j,j-1] = 1 / (xn[j]-xn[j-1])
        A[j,j] = 2 / (xn[j]-xn[j-1]) + 2 / (xn[j+1]-xn[j])
        A[j,j+1] = 1 / (xn[j+1]-xn[j])

        b[j] = 3 * ( (yn[j]-yn[j-1]) / (xn[j]-xn[j-1])**2 + (yn[j+1]-yn[j]) / (xn[j+1]-xn[j])**2 )
        
    v = MyGauss(A,b)
    # determine the coefficients
    for j in range(0,N):
        aj[j] = yn[j]
        bj[j] = v[j]
        cj[j] = 3*(yn[j+1]-yn[j])/(xn[j+1]-xn[j])**2 - (v[j+1]+2*v[j])/(xn[j+1]-xn[j])
        dj[j] = -2*(yn[j+1]-yn[j])/(xn[j+1]-xn[j])**3 + (v[j+1]+v[j])/(xn[j+1]-xn[j])**2

    # interpolate with spline
    for j in range(0,N):
        y[(xn[j]<=x) & (x<=xn[j+1])] = aj[j] + bj[j]*(x[(xn[j]<=x) & (x<=xn[j+1])]-xn[j]) +  \
              cj[j]*(x[(xn[j]<=x) & (x<=xn[j+1])]-xn[j])**2 + dj[j]*(x[(xn[j]<=x) & (x<=xn[j+1])]-xn[j])**3
        
    return y


a = 0
b = 3
nodes = 12
xn = np.linspace(a,b, nodes)
yn = func(xn)

bc_lower = 0.074  ## clamped lower boundary condition
bc_upper = -0.074

x = np.linspace(a,b,50)
P = spline(xn, yn, bc_lower, bc_upper, x)

plt.figure(dpi=200)
plt.plot(x,P, color='red', label = 'spline')
plt.scatter(xn, yn, color = 'blue', label = 'nodes')
plt.plot(x, func(x), color = 'green', label = 'actual')
plt.grid()
plt.legend()
plt.show()



