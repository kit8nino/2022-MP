import numpy as np
import math

a = len("Агафонов Михаил Геннадьевич")%5
print('Мой вариант:', a) # вариант 2 (методом простых итераций)

E = float(input("Введите точность эпсилон: ")) 
x = 0.6 # начальная точка, близкая к корню уравнения 

def lmd(x): # коэффициент лямбда = 1/f'(x_0)
    return 1.0/(2*x - 1.0/(1+x)) 

lmd_1 = lmd(x) 

def func(x):
    return x - lmd_1*(x**2 - math.log(1+x))

def precision(x): # условие на точность 
    return abs(func(x) - func(func(x)))

def solution(x, E):
    if precision(x) > E:
        return solution(func(x), E)
    else:
        return func(x)

print("Моё уравнение: f(x) = x**2 - ln(1+x) = 0 ")
print("Корень уравнения в окрестности точки x = ",x,'равен:', solution(x, E))  


















