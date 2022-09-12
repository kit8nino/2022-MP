import math as m

epsilon=float(input('Укажите точность: '))
x0=2.5
h=10**(-6)

def F(x): # функция получения следующего х
    return (m.tan(2*m.sin(x)))

def Condition(x1,x2): # проверка условия
    if abs(x1-x2)<epsilon:
        return True
    if abs(x1-x2)>epsilon:
        return False

def Algoritm(x): # метод итерации
    while not Condition(x,F(x)):
                        x+=h
    return F(x)

print('x=',Algoritm(x0))
