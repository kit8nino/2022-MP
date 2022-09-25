import math

eps = float(input("Enter the accuracy: "))

def f(x): 
    return (2-x) * math.exp(x)
 
def epsilon(b, a):
    return abs(b - a)
 
def halfdiv_method(a, b, c):
    
    if f(a) * f(b) < 0:
        if epsilon(b, a) > eps:
            
            if f(b) * f((b + a)/2) < 0:
                
                a = (b + a)/2 
                c = a 
                halfdiv_method(a, b, c)
                
            else:
                b = (b + a)/2 
                c = b
                halfdiv_method(a, b, c)
                
        else: 
            print('x =  ', c)

a = 0
b = 5
c = 1

halfdiv_method(a, b, c)
