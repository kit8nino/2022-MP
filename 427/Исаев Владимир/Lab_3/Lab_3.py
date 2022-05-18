import math
def cycle_for(x, eps,iter, foo):
    x0=x
    x=foo(x)
   
    if ((abs(x0 - x) > eps and iter < 20000) or iter==0):
        x0=x
        x=foo(x)
        
        
        cycle_for(x, eps,iter+1, foo)
       
    else:
        print("x = ",x0)
        return 

def my_func(x):
     return 1/(2*(x+1))
  
eps = float(input("Type what epsilon do you need?\n"))
cycle_for(1, eps,0 ,my_func)