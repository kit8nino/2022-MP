# -*- coding: utf-8 -*-
print("Номер задания:", len("Столяров Игорь Ильич")%5)
import math as m
a = 0.005
b = 10.0
h = 0.001
e = float(input('Введите точность вычисления корня'))
def f(x):
    return (m.log(x) + (x + 1)**3)
def stpr (xi):
    global h
    return (f(xi + h) - f(xi))/h
def ndpr(xi):
    return ((stpr(xi + h) - stpr(xi))/h)
def r(a,b):
    return abs(f(b) - f(a))
def resh():
    global a
    global b
    if (ndpr(a) < 0):
        a = a - (f(a)/stpr(a));
        print(a)
    if (ndpr(b) > 0):
        b = b - (f(b)/stpr(b));
        print(b)
    if (r(a,b) < e):
        return a
while (r(a,b) > e):
    resh()
print(f"f({0})=0",format(a))
    