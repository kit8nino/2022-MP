import math as m

def f(x):
    return m.log10(1+2*x)+x-2

def condition(a, b): #Условие запуска
    if f(a) * f(b) < 0: 
        return True
    else: 
        return False

def epsilon(x): #Модуль функции от х для критерия остановки цикла
    return abs(f(x))

def input_data(): 
    #Функция ввода для проверки, чтобы логарифм не имел отрицательного аргумента
    a = float(input("Начало интервала: "))
    b = float(input("Конец интервала: "))
    eps = float(input("Точность эпсилон: "))
    if a < 0 or b < 0 or eps < 0: 
        #Если что-то меньше нуля, запускаем новую итерацию функции ввода и возвращаем её значения
        print("Все числа должны быть положительные")
        return input_data()
    else : #Если всё ок, то возвращаем a b eps 
        return a, b, eps

def cycle_while(eps,x,a,b): #Цикл while через рекурсию функции
    if epsilon(x) > eps: #если abs(x)>eps
        print("X: ", x, " f(x): ", f(x))
        if(f(a) * f(x) < 0): 
             x = (x * f(a) - a * f(x)) / (f(a) - f(x))
        else:
            x = (x * f(b) - b * f(x)) / (f(b) - f(x))
        return cycle_while(eps,x,a,b) #Собственно, рекурсия
    else: 
        return x #Если критерий перестал соблюдаться, выходим из этой итерации, закрывая цикл

def chord(a, b, eps): #Метод хорд
    if condition(a,b):
        x = (a * f(b) - b * f(a)) / (f(b) - f(a))
        return cycle_while(eps,x,a,b) #Запускаем цикл
    else: #Если не соблюдается условия начала решения, выходим из функции
        return
print("Вариант ", len("Ефимов Кирилл Сергеевич")%5)
a, b, eps = input_data() #Вводим a b eps
chord(a,b,eps) #Запускаем метод хорд