print('Вариант №',len('Миронов Данила Алексеевич')%5)

import math
def newton(f,Df,x0,epsilon,max_iter):
    xn = x0
    for n in range(0,max_iter):
        fxn = f(xn)
        if abs(fxn) < epsilon:
            print('Найдено решение после',n,'итераций.')
            return xn
        Dfxn = Df(xn)
        if Dfxn == 0:
            print('Нулевая производная.  Решение не найдено.')
            return None
        xn = xn - fxn/Dfxn
    print('Превышено максимальное количество итераций. Решение не найдено.')
    return None

f=lambda x: math.log(x)+(x+1)**3
Df=lambda x:1/x+3*x**2+6*x+3
epsilon=float(input('Точность ввода: '))
approx=newton(f,Df,1,epsilon,10)
print(approx)