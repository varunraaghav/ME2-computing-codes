import numpy as np
A = np.array([[-4, 1, 0 , 1], [1, -4, 1, 0], [0, 1, -4, 1], [1, 0, 1, -4]])
b = [-2, -44, 238, -44]



u_guess = [100, 100, 100, 100]



def GaussSeidel(A, b, u):
    
    n = len(A[0])
         
    for i in range(0,n):
        temp = b[i]
        
        for j in range(0,n):
            if i!=j:
                temp -= A[i][j] * u[j]
    
        u[i] = np.round((temp / A[i][i]), 8)
            
       
      
        
    return u




######################    error parts below    

u = GaussSeidel(A, b, u_guess.copy())

u_prev = u_guess

error_limit = float(0.01) ### in percent value
Exit = int(0)
n = int(0)
 

while Exit != 1:
    
    u = GaussSeidel(A, b, u_prev.copy())
    n += 1
    Pass = int(0)
    for i in range (0, len(u_prev)):
        if abs((u[i] - u_prev[i])/u[i])*100 < error_limit:
            Pass += 1
            u_prev[i] = u[i]
        else:
            u_prev[i] = u[i]
    if Pass == len(u):
        Exit = 1
    else:
        Exit = 0
        
        
    


print(u, n)


