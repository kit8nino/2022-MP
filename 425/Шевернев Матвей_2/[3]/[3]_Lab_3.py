
import math as m


print("Мой вариант: ",len("Шевернев Матвей Вячеславович")%5)

def func(x):
    return m.log10(1+2*x)-2+x

E = float(input("Введите точность: "))

def hord(a, b, e):
    root = None
    if(func(a)*func(b)<0):
        
        while abs( b - a ) > e:
            c = a-func(a)*(b-a) / ( func(b)-func(a) )
            
            if func(c)==0 or abs(func(c)) < e:
                root = c
                break
            
            elif func(a)*func(c) < 0:
                b = c
                
            elif func(b)*func(c) < 0:
                a = c
                
    if root is None:
        print('Корень не найден')
    else:
        print('Корень уравнения :', root)


hord(1, 10, E) 