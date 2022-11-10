import numpy as np
import matplotlib.pyplot as plt
import math as mt

def TrNN(r,f,rp):
    d = np.ndarray(3)
    w = np.ndarray(3)
    for i in range(0,3):
        # determine the distances of rp from vertices
        d[i] = mt.sqrt( (r[i,0]-rp[0])**2 + (r[i,1]-rp[1])**2   )
        # determine the weight for this vertex
        w[i] = 1/ d[i]
    # interpolate with weights
    frp = ( w[0]*f[0] + w[1]*f[1] + w[2]*f[2] ) / (w[0]+[w[1]+w[2]])
    return frp


