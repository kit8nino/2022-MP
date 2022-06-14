# -*- coding: utf-8 -*-
"""
Created on Sun May 15 14:38:01 2022

@author: ДНС
"""
import math as m

v = len("Дручков Александр Дмитриевич")%5
print('Мой вариант:', v) # вариант 3 (метод хорд)

def func(x):
    return m.log10(1+2*x)-2+x

E = float(input("Input Epsilon: "))

def hord(a, b, e):
    it = 0
    root = None
    if(func(a)*func(b)<0):
        
        while abs( b - a ) > e:
            it += 1 
            c = a-func(a)*(b-a) / ( func(b)-func(a) )
            
            if func(c)==0 or abs(func(c)) < e:
                root = c
                break
            
            elif func(a)*func(c) < 0:
                b = c
                
            elif func(b)*func(c) < 0:
                a = c
                
    if root is None:
        print('Корень не найден')
    else:
        print('Корень X:', root)
        print('Значение функции в этой точке = ', func(root),'\n')   

hord(1, 10, E)      

