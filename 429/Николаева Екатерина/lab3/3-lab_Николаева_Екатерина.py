import math as m


print(len("николаева екатерина александровна")%5)

def f(x):
    return m.log10(1+2*x)+x-2

def condition(a, b): #Условие для начала решения
    if f(a) * f(b) < 0: 
        return True
    else: 
        return False

def epsilon(x):
    return abs(f(x))

def input_data(): 
    eps = float(input("Точность эпсилон: "))
    a = float(input("Начало интервала: "))
    b = float(input("Конец интервала: "))
    if a < 0 or b < 0 or eps < 0:
        print("Все числа должны быть положительные")
        return input_data()
    else :
        return a, b, eps

def cycle_while(eps,x,a,b):
    if epsilon(x) > eps:
        print("X: ", x, " f(x): ", f(x))
        if(f(a) * f(x) < 0): 
             x = (x * f(a) - a * f(x)) / (f(a) - f(x))
        else:
            x = (x * f(b) - b * f(x)) / (f(b) - f(x))
        return cycle_while(eps,x,a,b)
    else: 
        return x

#Метод хорд
def chord(a, b, eps):
    if condition(a,b):
        x = (a * f(b) - b * f(a)) / (f(b) - f(a))
        return cycle_while(eps,x,a,b)
    else:
        return

a, b, eps = input_data()
chord(a,b,eps)
