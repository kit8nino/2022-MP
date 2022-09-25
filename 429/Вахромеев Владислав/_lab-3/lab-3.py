import math as m


def f(x):
    return m.log10(1+2*x)+x-2

def condition(a, b): 
    if f(a) * f(b) < 0: 
        return True
    else: 
        return False

def eps(x):
    return abs(f(x))

def inputing(): 
   
    a = float(input("Начало интервала: "))
    b = float(input("Конец интервала: "))
    ep = float(input("Точность эпсилон: "))
    if a < 0 or b < 0 or ep < 0: 
              print("Все числа должны быть положительные")
              return inputing()
    else : 
        return a, b, ep

def cycle(ep,x,a,b):
    
    if eps(x) > ep: 
        
        if(f(a) * f(x) < 0): 
            
             x = (x * f(a) - a * f(x)) / (f(a) - f(x))
        else:
            x = (x * f(b) - b * f(x)) / (f(b) - f(x))
        return cycle(ep,x,a,b) 
        
    else: 
        print("X: ", x, " f(x): ", f(x))
        return x 
    
    print("X: ", x, " f(x): ", f(x))
    
    
def m_chord(a, b, ep): #mетод хорд
    if condition(a,b):
        x = (a * f(b) - b * f(a)) / (f(b) - f(a))
        return cycle(ep,x,a,b) 
    else: 
        return
a, b, ep = inputing() 
m_chord(a,b,ep) 
