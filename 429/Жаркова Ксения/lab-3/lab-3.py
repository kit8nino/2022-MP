import numpy as np

a = 2.5
b = 2.6

x = 10

def func(x):
    return np.tan(2*np.sin(x))

def epsilon(x):    
    return abs(func(x)-func(func(x))) 

def solve_equation(x, presition):
    if epsilon(x) > presition:
        return solve_equation(func(x), presition)
    else:
        return func(x)

print("\nEquation: 2 * sin(x) - arctan(x) = 0")
presition = float(input("Enter the precition:\n"))

root=solve_equation(x, presition)

if a <= root <= b:
    print("\nx ∈ (",a,",",b,")")
    print("x = ", root)
else:
    print("x = ", root)
    print("The root is not on the given segment!")