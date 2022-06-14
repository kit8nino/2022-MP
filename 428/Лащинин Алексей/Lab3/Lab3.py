import math as m 
epsilon=float(input('Specify the assucrancy'))
a=0
b=100
def F(x):
    return (m.log(1+2*x)-2+x)
def C(a,b):
    return((a+b)/2)

def Algoritm(a,b):
    while epsilon<(abs(b-a)/2):
        if((F(a)*F(C(a,b)))<0):
            b=C(a,b)
        else:
            a=C(a,b)
        
    return ((a+b)/2)
    
print('x=',Algoritm(a,b))
    