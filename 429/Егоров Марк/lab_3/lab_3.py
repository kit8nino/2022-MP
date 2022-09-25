import math as m

print('Вариант номер', len("Егоров Марк Андреевич")%5)

epsilon=float(input("Точность эпсилон:"))

def f(x):
        return (2-x)*m.exp(x)

def half(y,x):
    return (y+x)/2

def M_dih(y,x,a):
        if(abs(f(half(y,x)-f(y))) < epsilon):
                print("Корень уравнения: x= ",half(y,x))
        elif(f(half(y,x)*a)>0):
            M_dih(half(y,x),x,a)
        else:
            M_dih(y,half(y,x),a)

a=1
y=1
x=3

M_dih(y,x,a)
