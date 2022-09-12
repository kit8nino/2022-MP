import numpy as np

# 3 - horda method
# np.log(1+2*x,10) = 2 - x


def F(x):
    return np.log10(1+2*x) - 2 + x  

def F1(x):
    res=2/(np.log(10)*(1+2*x))+1
    print(res)
    return res

def Method(a, b,precision):
    x0 = (a + b) / 2
    xn = F(x0)
    xn1 = xn - F(xn) / F1(xn)
    while abs(xn1 - xn) > precision:
        xn = xn1 
        xn1 = xn - F(xn) / F1(xn)
    print(xn1)
    return xn1




x=float(input())
a=float(input())
b=float(input())

precision = float(input("Type what precision do you need?\n"))

F(x)
F1(x)
Method(a, b,precision)

