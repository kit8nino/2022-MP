print('мой вариант:', len("Афиногенов Вадим Игоревич")%5)

import numpy as np

# сама функция
def f(x):
    y = np.log(x) + (x + 1)**3
    return y

# производная f(x)
def f_strih(x):
    return 1/x + 3*(x + 1)**2

# метод касательных, принимает начальное значение и точность,
# возвращает полученное значение и количество итераций
def tangent_method(x, E):
    q = 0
    while (abs(f(x)) > E):
        x = x - f(x)/f_strih(x)
        q += 1
    return x, q
    

E = input('точность: ')
E = float(E)
x = 1

x, q = tangent_method(x, E)
    

print("количество итераций:", q)
print("х =", x)
print("f(x) =", f(x))