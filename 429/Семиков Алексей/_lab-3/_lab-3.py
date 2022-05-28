import math as m 

def my_func(x):
    return 2 * m.sin(x) - m.atan(x)

def func_iter(x):
    return x - 0.542699 * (2 * m.sin(x) - m.atan(x))

def method_iter(x, e, i):
    rez = x
    x = func_iter(x)
    i = i + 1
    if abs(x - rez) < e:
        print("Result: ", x)
        print("Iteration: ", i)
        return x
    else:
        method_iter(x, e, i)

x = 2.6
i = 1
e = float(input("With what accuracy to find the root? "))
method_iter(x, e, i) 
