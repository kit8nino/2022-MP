#!/usr/bin/env python
# coding: utf-8

# In[1]:


#сделали Миронов и Поздоровкин
from generator_simple import Generator_simple
import numpy as np

class Generator_complex(Generator_simple):
    def __init__(self,f,y_n,t,f_0,Ampl):  
        self.x_n=np.arange(0,t,1./f_0)
        self.f= f/20  
        self.Am0=2
        self.z=1
        self.F0=10
        self.y_n=np.array(y_n)
        self.f_0=f_0
        self.Ampl=Ampl
    def get_f(self,c):
        self.f=self.f/c
    def envel(self):
        self.save_yn=self.y_n
        self.y_n=(self.Am0+self.z*self.y_n)*np.cos(self.f*self.x_n+self.F0*np.pi)
        return self.y_n
    def generator_c(self,t): 
        x_n=np.arange(self.x_n[len(self.x_n)-1],self.x_n[len(self.x_n)-1]+t,1./self.f_0)
        for i in x_n:
            if self.x_n[len(self.x_n)-1]+t>=i:
                yield (self.Am0+self.z*self.save_yn)*np.cos(self.f*i+self.F0*np.pi)


# In[ ]:




