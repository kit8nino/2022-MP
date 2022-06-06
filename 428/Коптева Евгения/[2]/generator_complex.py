#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from generator_simple import Generator_simple
import numpy as np

class Generator_complex(Generator_simple):
    def __init__(self,fr,y_new,time,fr_0,Ampl):  
        self.x_new=np.arange(0,time,1./fr_0)
        self.fr= fr/20  
        self.Am0=2
        self.z=1
        self.Fr0=10
        self.y_new=np.array(y_new)
        self.fr_0=fr_0
        self.Ampl=Ampl
    def get_f(self,c):
        self.fr=self.fr/c
    def envel(self):
        self.save_yn=self.y_new
        self.y_new=(self.Am0+self.z*self.y_new)*np.cos(self.fr*self.x_new+self.Fr0*np.pi)
        return self.y_new
    def generator_c(self,time): 
        x_new=np.arange(self.x_new[len(self.x_new)-1],self.x_new[len(self.x_new)-1]+time,1./self.fr_0)
        for i in x_new:
            if self.x_new[len(self.x_new)-1]+time>=i:
                yield (self.Am0+self.z*self.save_yn)*np.cos(self.fr*i+self.Fr0*np.pi)

