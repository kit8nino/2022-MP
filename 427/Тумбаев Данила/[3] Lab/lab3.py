import numpy as np


print('Номер задания:', len("ТумбаевДанилаАлексеевич")%5)
print('Метод хорд')

def function_add_e():
    e = float(input("Введите точность: "))
    return e;

def f(x):
    return np.log10(1+2*x)-2+x

n=0
def while_block(a,b,e):
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
        return while_block(a, b, e)


def hord(a, b, e):
    root=None
    if(f(a)*f(b)<0):
        '''
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
        '''
        root = while_block(a, b, e)
    if root is None:
        print('Корень не найден')
    else:
        print(f'Корень: x = {root}')
        print('Количество итераций: n = ', n)
        print('Значнеие функции F(x) = ', f(root),'\n')   


hord(0, 2, function_add_e())