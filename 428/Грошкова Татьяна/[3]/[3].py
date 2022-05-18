import numpy as np
import math

E=float(input("Введите точность вычислентя для функции f(x)=(2-x)exp(x):"))
def f(x):
	return (2-a)*math.exp(a)
def half(x0,x):
	return (x0+x)/2
a=1
def M_dih(x0,x,a):
        if f(x)*f(x0)<0:
            if abs(x-x0)>E:
                if f(x)*f(half(x0,x))<0: 
                    x0=half(x0,x)
                    a=x0
                    M_dih(x0,x,a)
                else:
                    a=half(x0,x)
                    a=x
                    M_dih(x0,x,a)
            else: 
                print('Корень уравнения: x~',a)
x0=1
x=7
M_dih(x0,x,a)
