
import numpy as np


F = lambda x: np.log10(1+2*x) - 2 + x 

F1 = lambda x: 2/(np.log(10)*(1+2*x))+1

def Horda(a, b,precision):
    x0 = (a + b) / 2
    xn = F(x0)
    xn1 = xn - F(xn) / F1(xn)
    while abs(xn1 - xn) > precision:
        xn = xn1 
        xn1 = xn - F(xn) / F1(xn)
    print(xn1)
    return xn1

a=1
b=4

precision = float(input(" Input your presisison?"))

Horda(a, b,precision)


