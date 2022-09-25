import numpy as np
####################################
print('мой вариант:', len("Головастиков  Александр Сергеевич")%5)
print("корень теоретический х = 1,41646835240")

def f(x):
    y = np.log10(1+2*x)-2+x
    return y
####################################

def method_hord (a,b,x,E):
    k = 0
    while(abs(f(x)) > E):

        if(f(a)*f(b) < 0):
            x = a - f(a)*(b - a)/(f(b) - f(a))

        if(f(a)*f(x) < 0):
            b = x

        if(f(b)*f(x) < 0):
            a = x

        k = k + 1
    return x, k
a = 0
b = 4
print("введите эпсилон: ")
E = float(input())
x = 2
x, k = method_hord(a,b,x,E)
print("корень методом хорд х = ", x)
print("f(x) = ", f(x))
print("количество операций: ", k, "\n")