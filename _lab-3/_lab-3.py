import numpy as np

# No cycles, only recursion
def cycle_for(i, i_max, foo):
    if i==i_max:
        return
    else:
        foo()
        cycle_for(i+1, i_max, foo)

def my_func():
    print("I'm doing something strange")

print("Cycle via recursion")
cycle_for(0, 10, my_func)

# No variables, only constants
a = 5 #forever
b = "Eternity" # forever

# Iterations method
# x**3 + .3*x**2 - 4.5*x + 1.1 = 0
# transform to x = (x**3 + .3*x**2 + 1.1)/4.5
# take some initial x0. let it be 7

x = -.1
def equation_func(x):
    return (x**3 + .3*x**2 + 1.1)/4.5

def epsilon(x):
    return abs(equation_func(x) - equation_func(equation_func(x)))

def solve_equation(x, presition):
    if epsilon(x) > presition:
        return solve_equation(equation_func(x), presition)
    else:
        return equation_func(x)

print("\nEquation: x**3 + .3*x**2 -4.5x + 1.1 = 0")
presition = float(input("Type what presition do you need?\n"))
print("x = ", solve_equation(x, presition))
