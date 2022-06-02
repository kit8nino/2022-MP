import math
import numpy as np

print('Вариант:',len("Карасев Андрей Александрович")%5)

E = float(input('Введите точность вычислений: '))

limitLeft = 0
limitRight = 5
limitResLeft = limitLeft
limitResRight = limitRight
width = 20

def func(x):
    return (np.log10(1+2*x)-2+x)

def func1(x):
    return (2/(np.log(10)*(1+2*x))+1)

def hord(a, b, E):
    iteration = 0
    f = 1
    f0 = func(a)
    res = b
    while (math.fabs(f) > E):
        iteration += 1
        f = func(res)
        res = res - f / (f - f0)*(res - a)
    print("iterations: ", iteration)
    return (res)



for a in range(limitLeft, limitRight): 
    for b in range(a, limitRight):
        if ((func(a)*func(b) < 0) and (func1(a)*func1(b) > 0)):
            if ((b - a) <= width):
                limitResLeft = a
                limitResRight = b
                width = b - a
            
print("a: ", limitResLeft, " ,b:", limitResRight)    
    
xHord = hord(limitResLeft, limitResRight, E)
print("x: ", xHord)
print("f(x): ", func(xHord))
