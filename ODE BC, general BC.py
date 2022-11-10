# session 8, task B - Solving with gauss seidel


import math 
import numpy as np
import matplotlib.pyplot as plt




def func(x):
    f = float(2 * x)
    g = int(2)
    p = float(np.cos(3*x))
    
    return f , g , p





def myodebc (xa, xb, ya, yb, N):
    h = (xb - xa) / N
    
    
    x = np.linspace(0, np.pi, N+1)
    
    P = np.zeros(N+1)
    P[0] , P[N] = ya, yb
    
    
    
    
    M = np.zeros((N+1, N+1))
    M[0][0] , M[N][N] = int(1) , int(1)
    

    for i in range(1, N):
        
        
            
        f , g , p = func(x[i])
        
        M[i,i-1] =  (  1/(h**2) - (f/(2*h))  )
        M[i,i] = (  g  - (2/(h**2)) )
        M[i,i+1] = (  1/(h**2) + (f/(2*h)) )
                         
        P[i] = p                 
                         
                         
    return M , P , x


ya = 1.5
yb = 0
N = 100

xa = 0
xb = np.pi

M , P , x = myodebc(xa, xb, ya, yb, N)


################# solving using Gauss-Seidel methods : ########################





def GaussSeidel(A, b, u):
    
    n = len(A[0])
         
    for i in range(0,n):
        temp = b[i]
        
        for j in range(0,n):
            if i!=j:
                temp -= A[i][j] * u[j]
    
        u[i] = (temp / A[i][i])
            
       
      
        
    return u


## put starting value for u guess (inside u)

u = np.zeros(N+1)

u = GaussSeidel(M.copy(), P.copy(), u.copy())



for count in range(0, 500):
    u = GaussSeidel(M, P, u)


plt.figure(dpi=1200)
plt.plot(x, u, '.', color = 'green')
plt.title('Using Gauss-Seidel and number of iterations: 500')
plt.xlabel('x')
plt.ylabel('y')



# u_prev = u

# error_limit = float(0.01) ### in percent value
# Exit = int(0)
# n = int(0)
 

# while Exit != 1:
    
#     u = GaussSeidel(M.copy(), P.copy(), u_prev.copy())
#     n += 1
#     Pass = int(0)
#     for i in range (0, len(u_prev)):
        
#         if u[i] != 0:    
            
#             if abs((u[i] - u_prev[i])/u[i])*100 < error_limit:
#                 Pass += 1
#                 u_prev[i] = u[i]
#             else:
#                 u_prev[i] = u[i]
        
#         else:
#             Pass += 1
            
            
#     if Pass == len(u) or Pass== (len(u) + 1):
#         Exit = 1
#     else:
#         Exit = 0
        
        
        
        



