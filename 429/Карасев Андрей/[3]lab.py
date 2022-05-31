print('Вариант:',len("Карасев Андрей Александрович")%5)
import math
import numpy as np
E = float(input('Введите точность вычислений: '))
s=0
n=0
def func(x): # основная функция
    return(x*2**x-np.log(x+1))

x=np.arange(-E,2,E)
y=func(x)

def func2(x): # приведение функции к явному виду
    return np.sqrt(np.log(x+1))

xn = 1 
xp = 0 
while np.abs(xn-xp) > E: # метод простых интераций
    s+=1
    xp=xn
    xn=func2(xp)

if(xn <= 1):
    print('x - один из корней вне области допустимых значений(по определнию логарифма)')    
print('x = ', xn) # значение аргумента(корня уравнения)
print('F(x) = ',func(xn)) # значение функции в этой точке
print('Iteration =', s) # количество интераций(хз зачем, но почему бы и нет)
