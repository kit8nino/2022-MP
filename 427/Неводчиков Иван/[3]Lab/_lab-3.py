import numpy as np   
def f(x):
    return np.log10(1+2*x)-2+x
def info():
    print('Номер задания:', len("Неводчиков Иван Владимирович")%5)
    print('Метод хорд')

def Evv():
    info()
    e = float(input("Введите точность: "))
    return e;
n=0

def rek(a,b,e):
    global n
    n+=1
    if ((a-b)<=e):

        c=a-f(a)*(b-a)/(f(b)-f(a))
        if f(c)==0 or abs(f(c))<e:
            root=c
            return root
        elif f(a)*f(c)<0:
                b=c
        elif f(b)*f(c)<0:
                a=c 
        return rek(a, b, e)
    
def hord(a, b, e):
    root=None
    if(f(a)*f(b)<0):
        root = rek(a, b, e)
    if root is None:
        print('Корень не найден')
    else:
        print('Моё уравнение: f(x) = lg(1+2x)-2+x')
        print(f'Корень: x = {root}')
        print('Количество итераций: n = ', n)
        print('Значнеие функции F(x) = ', f(root),'\n')   

hord(0, 2, Evv())