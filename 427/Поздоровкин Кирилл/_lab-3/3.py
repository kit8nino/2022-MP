#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import math

print('Номер задания:', len("ПоздоровкинКириллРоманович")%5)

epsilon=float(input("Точность вычисления:"))
def f(x):
        return (2-x)*math.exp(x)
def half(y,x):
    return (y+x)/2
a=1
def M_dih(y,x,a):
        if(abs(f(half(y,x)-f(y))) < epsilon):
                print("Корень уравнения: x= ",half(y,x))
        elif(f(half(y,x)*a)>0):
            M_dih(half(y,x),x,a)
        else:
            M_dih(y,half(y,x),a)
        
                
y=1
x=3
M_dih(y,x,a)


# In[ ]:





# In[ ]:




