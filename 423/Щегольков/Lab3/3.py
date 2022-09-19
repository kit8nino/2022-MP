import math

c = len("Щегольков Михаил Андреевич")%5
print('Мой вариант:', c)

print('Метод половинного деления')

eps = float(input("Введите точность вычисления: "))

x = 0
y = 5
a = 1

def f(x):
    return ((2-x)*math.exp(x))

def epsilon(y, x):
    return abs(y - x)

def c_func(y, x):
    return (y + x) / 2

def dihotomia(x, y, a):
    if f(x) * f(y) < 0:
        if epsilon(y,x)>eps:
            if f(y)*f(c_func(y, x))<0:
                x = c_func(y,x)
                a = x
                dihotomia(x, y, a)
            else:
                y = c_func(y, x)
                c = y
                dihotomia(x, y, a)
        else:
            print("Моё уравнение: f(x) = (2-x)*e^(x)")
            print('Корень уравнения: ', a)
dihotomia(x, y, a)
