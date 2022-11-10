

import matplotlib.pyplot as plt
import numpy as np
import math
import random


def func(x):
    y = x**2 + (x-2)**3 - 4
    return y

def func_der(x):
    y = 2*x + 3*(x-2)**2
    return y


def NewtonRaphson(x_guess,tol,i):
    while abs(func(x_guess)) > tol :
        i = i + 1
        
        x_next = x_guess-func(x_guess)/func_der(x_guess)  # Newton-Raphson equation
    
        x_guess = x_next
        
    return x_guess, i
    
    
tol = 0.01  # Tolerance
i = 0  # Iteration counter
x_guess = 32  # Initial guess

print(NewtonRaphson(x_guess, tol, i))