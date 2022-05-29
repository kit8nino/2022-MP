#!/usr/bin/env python
# coding: utf-8

# In[12]:


print('Вариант №',len('Клоканов Артём Сергеевич')%5)


# In[25]:


import math as m

epsilon=float(input('Specify the accurancy'))
x0=2.5
h=10**(-6)

def F(x): # функция получения следующего х
    return (m.tan(2*m.sin(x)))

def Condition(x1,x2): # проверка условия
    if abs(x1-x2)<epsilon:
        return True
    if abs(x1-x2)>epsilon:
        return False

def Algoritm(x): # сам метод итерации
    while not Condition(x,F(x)):
                        x+=h
    return F(x)

print('x=',Algoritm(x0))
                    

    


# In[ ]:




