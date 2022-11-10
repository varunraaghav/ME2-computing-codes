

import matplotlib.pyplot as plt
import numpy as np
import math

##### All the functions required for Jacobian matrix
def u(x,y):
    res = x**2 + 1 - y
    return res

def v(x,y):
    res = 2*np.cos(x) - y
    return res

def du_dx(x,y):
    res = 2*x
    return res

def du_dy(x,y):
    res = -1
    return res

def dv_dx(x,y):
    res = -2*np.sin(x)
    return res

def dv_dy(x,y):
    res = -1
    return res




def NewtonRapshonCoupled(A,tol):
    
    A_next = [A[0]+7*tol , A[1]+7*tol]    #### making the n+1 guess, greater than tolerance so that function runs atleast once
    diff1 = abs(A_next[0] - A[0])
    diff2 = abs(A_next[1] - A[1])
    count = 0
    
    while (diff1 > tol) or (diff2 > tol):### iterating using NR formula to get A_n+1
        A = A_next
        J = np.array([[du_dx(A[0],A[1]),du_dy(A[0],A[1])],[dv_dx(A[0],A[1]),dv_dy(A[0],A[1])]])
        J_inv = np.linalg.inv(J)
        
        b = np.array([u(A[0],A[1]), v(A[0],A[1])])
        
        A_next = A - np.dot(J_inv,b)
        diff1 = abs(A_next[0] - A[0])
        diff2 = abs(A_next[1] - A[1])
    
        count += 1
        
    print(count)

    return A_next


A = [2735, 21]
tol = 0.001

solutions = NewtonRapshonCoupled(A, tol)
print("x_root = ", solutions[0] , ' ; y_root = ' , solutions[1])