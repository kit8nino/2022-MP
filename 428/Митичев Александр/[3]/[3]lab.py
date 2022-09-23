import math
E=float(input("Введите точность вычислентя ф-и f(x)=(2-x)exp(x):"))
def f(x):
        return (2-x)*math.exp(x)
def pol(x0,x):
    return (x0+x)/2
a=1.
def M(x0,x,a):
        if(abs(f(pol(x0,x)-f(x0))) < E):
                print("x = ",pol(x0,x))
        elif(f(pol(x0,x)*a)>0):
            M(pol(x0,x),x,a)
        else:
            M(x0,pol(x0,x),a)
        return()                
x0=1.
x=3.
M(x0,x,a)