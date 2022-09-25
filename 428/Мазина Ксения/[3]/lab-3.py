import math as m 
print('Вариант №', len("Мазина Ксения Максимовна")%5)
x = 2.6
i = 1
eps = float(input("Введите точность eps: "))

def F(x):
    return x - 0.542699 * (2 * m.sin(x) - m.atan(x))

def method_iter(x, eps, i):
    rez = x
    x = F(x)
    i += 1
    if abs(x - rez) < eps:
        print("Корень уравнения 2sin(x)-arctg(x)=0: ", x)
        print("Количество итераций: ", i)
        return x
    else:
        method_iter(x, eps, i)

method_iter(x, eps, i) 
