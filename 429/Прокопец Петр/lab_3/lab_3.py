import math as m

#import numpy as np
#import matplotlib.pyplot as plt
#x_arr = np.arange(-8, 8,0.1)
#y_arr = np.log10(1+2*x_arr)-2+x_arr

#plt.plot(x_arr, y_arr, 'b')
#plt.show()

def func(x):
    return m.log10(1+2*x)-2+x

def hord(x_left, x_right, eps):
    a = x_left
    b = x_right
    x = None
    if(func(a)*func(b)<0):
        
        while abs( b - a ) > eps:
            c = a-func(a)*(b-a) / ( func(b)-func(a) )
            
            if func(c)==0 or abs(func(c)) < eps:
                x = c
                break
            
            elif func(a)*func(c) < 0:
                b = c
                
            elif func(b)*func(c) < 0:
                a = c
    else:
        print("Функция не пересекает ось абсцисс на заданном участке")
         
    if not (x is None):
        return x
    
eps = float(input("Точность исчисления: "))
x_left = -0.4
x_right = 4

x_result =  hord(x_left ,x_right, eps) 


print("X:", x_result)
print("Значение функции в X: ", func(x_result))