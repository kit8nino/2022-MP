#Плахов Антон. Вариант 1. Метод половинного деления

import numpy as np

def f(x):
    return (2-x)*np.exp(x)

#main
print("Введите точность измерений")

E=float(input())
x1=1
x2=3
a=1
while abs(f(x2)-f(x1))>E:
    if(f(a)>0):
        x1=a
        a=(x1+x2)/2
    else:
        x2=a
        a=(x1+x2)/2

print("x = ",a)
