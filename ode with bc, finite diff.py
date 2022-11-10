# session 8, task A 


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
    
    
    x = np.linspace(xa, xb, N+1)
    
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



#answer = np.dot(np.linalg.inv(M), P)
answer = np.linalg.solve(M,P)

# print(answer)

plt.figure(dpi=1200)
plt.plot(x, answer, '.')
plt.title('Using numpy linalg.solve')
plt.xlabel('x')
plt.ylabel('y')

