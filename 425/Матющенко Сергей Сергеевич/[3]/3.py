print('Вариант №',len('Матющенко Сергей Сергеевич')%5)
import numpy as np
def f(x):
    return (2-x)*np.exp(x)
def c(x0,x):
    return (x0+x)/2
def solve(x0,x,a):
    if abs(f(c(x0,x)-f(x0)))<E:
        print("Корень уравнения: x = ",c(x0,x))
    elif(f(c(x0,x)*a)>0):
        solve(c(x0,x),x,a)
    else:
        solve(x0,c(x0,x),a)
    return()
E=float(input("Введите точность:"))
a=1
x0=1
x=3
solve(x0,x,a)