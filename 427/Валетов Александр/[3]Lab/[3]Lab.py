import numpy as np   
e = 0.0
def f(x):
    return np.log10(1+2*x)-2+x

e = float(input("Введите точность: "))

def hord(a, b, e):
    n = 0
    root=None
    if(f(a)*f(b)<0):
        while abs(a-b)>e:
            n+=1
            c=a-f(a)*(b-a)/(f(b)-f(a))
            if f(c)==0 or abs(f(c))<e:
                root=c
                break
            elif f(a)*f(c)<0:
                b=c
            elif f(b)*f(c)<0:
                a=c
    if root is None:
        print('Корень не найден')
    else:
        print(f'Корень: x = {root}')
        print('Количество итераций: n = ', n)
        print('Значнеие функции F(x) = ', f(root),'\n')   

hord(0, 2, e) 