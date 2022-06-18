#Плахов Антон. Вариант 1. Метод половинного деления

import numpy as np

def f(x):
    return (2-x)*np.exp(x)

def c(X,x):
    return (X+x)/2

def solution(X,x,a):
    if abs(f(c(X,x)-f(X)))<E:
        print("x = ",c(X,x))
    elif(f(c(X,x)*a)>0):
        solution(c(X,x),x,a)
    else:
        solution(X,c(X,x),a)
    return()

#main
print("Введите точность измерений")

E=float(input())
a=1
X=1
x=3

solution(X,x,a)
