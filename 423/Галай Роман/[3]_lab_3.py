#Делал в паре с Андреем Чебыровым
import random
import cmath as mt
print('Вариант №',len('Галай Роман Олегович')%5)
f=lambda x: mt.log(x)+(x+1)**3
def differ(func, x: float, epsilon: float):
return (func(x + epsilon / 2.) - func(x - epsilon / 2.)) \
/ epsilon


def newton(func, x: float, epsilon: float):
try:
div = differ(func, x, epsilon)
if (div == 0.):
return newton(func, (x + epsilon / 2 * (-1) ** (random.random())).real, epsilon)
new_x = x - func(x) / div
if abs(new_x - x) > epsilon:
return newton(func, new_x, epsilon)
else:
return new_x
except:
return x

epsilon=float(input('Точность ввода: '))
approx=newton(f,1.,epsilon)
print(approx)