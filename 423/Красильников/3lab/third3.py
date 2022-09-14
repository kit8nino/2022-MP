import math as m

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
        return 
    
eps = float(input("Введите точность исчисления: "))
x_left = -0.4
x_right = 4

x_result =  hord(x_left ,x_right, eps) 


print("Значение X:", x_result)
print("Значение функции в X: ", func(x_result))