print(len("Скворцов Николай Васильевич")%5)
import numpy as np ## подключаем библиотеки
import matplotlib.pyplot as plt
import math

def f(y):
        return math.sqrt(np.log(y+1))
def iter(y, e, i):
    temp =y
    y = f(y)
    i=i + 1
    if abs(temp - y) > e:
        iter(y, e, i)
    else:
        print("Результат: x= ",y,"Кол-во итераций=", i )
e = float(input("Введите точность вычисления:"))
i=0
y=2.6
i=1
iter(y, e, i)
