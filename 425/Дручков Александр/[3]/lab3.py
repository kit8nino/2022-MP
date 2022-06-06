# -*- coding: utf-8 -*-
"""
Created on Sun May 15 14:38:01 2022

@author: ДНС
"""

import numpy as np
import matplotlib.pyplot as plt 

v = len("Дручков Александр Дмитриевич")%5
print('Мой вариант:', v) # вариант 3 (метод хорд)
def func(x):
    return np.log10(1+2*x) + x - 2

x_ar = np.linspace(0,2,50)


def eq_func(x):
    return 2 - np.log10(1+2*x)

a = float(input("Введите начало интервала: "))
b = float(input("Введите конец интервала: "))
eps = float(input("Введите точность: "))

x = (a*func(b) - b*func(a))/(func(b) - func(a))

def funcbz(a,x):
    return (x*func(a) - a*func(x))/(func(a) - func(x))
def funcoz(b,x):
    return (x*func(b) - b*func(x))/(func(b) - func(x))
def funcab(a,b):
    return func(a)*func(b)
def funcax(a,x):
    return func(a)*func(x)

if funcab(a,b) < 0:
    while abs(func(x))>eps:
        if(funcax(a,x) < 0):
            x = funcbz(a,x)
        else:
            x = funcoz(b,x)
            
plt.plot(x_ar, func(x_ar))            
plt.plot(x,func(x),marker = 'o')
plt.grid()
plt.show()                     
print("Уравнение:  np.log10(1+2*x) + x - 2  = 0 ")
print("X(корень): ", x, "f(x): ",func(x))           

