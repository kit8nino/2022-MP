#!/usr/bin/env python
# coding: utf-8

# In[23]:


import numpy as np
import math

print('Variant: ', len("Миронов  Андрей Алексеевич")%5)

Eps=float(input("Enter the calculation accuracy for the function f(x)=(2-x)exp(x): "))
def f(x):
        return (2-x)*math.exp(x)
def half(x0,x):
    return (x0+x)/2
a=1
def M_dihotomia(x0,x,a):
        if(abs(f(half(x0,x)-f(x0))) < Eps):
                print("Корень уравнения: x= ",half(x0,x))
        elif(f(half(x0,x)*a)>0):
            M_dihotomia(half(x0,x),x,a)
        else:
            M_dihotomia(x0,half(x0,x),a)
        
                
x0=1
x=3
M_dihotomia(x0,x,a)


# In[ ]:





# In[ ]:




