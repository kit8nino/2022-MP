import numpy as np
import random

def fx(x):
    return np.sqrt(np.log(x + 1))

def prost(eps, x0):
    x_save = x0
    x0 = fx(x0)
    if(abs(x_save - x0) > eps):
        return prost(eps, x0)
    else:
        return x0
    return x0
    

print(prost(float(input()), (random.random() )))
    