from sympy import *
x = Symbol('x')

print("Вариант - ",len("ГалкинМаксимЕвгеньевич")%5)

def Cycle_func(x0,c,eps,y,dy,i):
    if(abs(c-x0) >= eps):
        d = x0 - float(y(x0)/dy(x0))  #Расчет последующих точек с постоянным пересчетом производной
        c = x0 #предыдущая точка
        x0 = d #Фиксация новой точки
        i += 1
        return Cycle_func(x0,c,eps,y,dy,i)
    else:
        return x0,i

def Metod_ProstoiIteracii(eps, f):
    x0 = 10.0 #Начальная точка
    c = 1000.0 #Произвольная вспомогательная переменная для условия заканчивания цикла
    i = 0 #Счётчик
    y = lambdify(x, f)
    dy = lambdify(x, diff(f, x))
        
    return Cycle_func(x0,c,eps,y,dy,i)  
     
f = log(x+1) - x**2 #Уравнение

eps = float(input("Введите точность: "))
res,count = Metod_ProstoiIteracii(eps, f)
print("x = ",res)
print("Итерации - ",count)

