import numpy as np
import math

a = len("Агафонов Михаил Геннадьевич")%5
print('Мой вариант:', a) # вариант 2 (методом простых итераций)

E = float(input("Введите точность эпсилон: ")) 

x = 0.6 # начальная точка (начальное условие)
def func(x):
    return 1.5 - math.log(1+x)

def precision(x): # условие на точность 
    return abs(func(x) - func(func(x)))

def solution(x, E):
    if precision(x) > E:
        return solution(func(x), E)
    else:
        return func(x)

print("Моё уравнение: f(x) = x + ln(1+x) - 1.5 = 0 ")
print("Корень уравнения: x = ", solution(x, E))  