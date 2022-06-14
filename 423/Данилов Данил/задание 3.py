import math

print(len('Данилов  Данил  Алексеевич')%5)
print('Option:', 1)
print('Half division method')

eps = float(input("Enter: "))

x = 1 # начальная точка
y = 7 # конечная точка

c = 1

def f(x):
    return ((2-x)*math.exp(x))

def epsilon(y, x):
    return abs(y - x)

def c_func(y, x):
    return (y + x) / 2

def dihotomia(x, y, c):
    if f(x) * f(y) < 0:
        if epsilon(y,x)>eps:
            if f(y)*f(c_func(y, x))<0:
                x = c_func(y,x)
                c = x
                dihotomia(x, y, c)
            else:
                y = c_func(y, x)
                c = y
                dihotomia(x, y, c)
        else:
            print("My equation: f(x) = (2-x)*math.exp(x)")
            print('Root of the equation: ', c)
dihotomia(x, y, c)
