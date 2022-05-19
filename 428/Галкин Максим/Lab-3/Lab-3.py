from sympy import *

x = Symbol('x')

print("Вариант - ",len("ГалкинМаксимЕвгеньевич")%5)

def Metod_ProstoiIteracii(eps, y, dy):
    x0 = 10.0 #Начальная точка
    c = 1000.0 #Произвольная вспомогательная переменная для условия заканчивания цикла
    i = 0 #Счётчик
    d = 0.0
    
    while(abs(c-x0) >= eps):
        d = x0 - float(y(x0)/dy(x0))  #Расчет последующих точек с постоянным пересчетом производной
        c = x0 #предыдущая точка
        x0 = d #Фиксация новой точки
        i += 1

    print ("Корень -", x0)
    print ("Итерации -", i)
    
f = log(x+1) - x**2 #Уравнение

y = lambdify(x, f)
dy = lambdify(x, diff(f, x))

eps = float(input("Введите точность: "))
Metod_ProstoiIteracii(eps, y, dy)