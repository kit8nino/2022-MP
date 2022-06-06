#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#сделали Миронов и Поздоровкин
import numpy as np
from scipy import signal

class Generator_simple():
    def __init__(self,f,f_0,t,Ampl):
            self.f=f
            self.f_0=f_0
            self.t=t
            self.Ampl=Ampl
            self.count=0
    def Signal_Harmonic(self,t):
        self.x_n=np.arange(0,t, 1./self.f_0)
        for i in range(len(self.x_n)):
            yield (self.Ampl*np.cos(self.x_n[i]*self.f))
    def Signal_SHIM(self,t,pr_cycles):
        if t<=0:
            t=self.t
        pr=pr_cycles
        dt=1/self.f_0
        x_n=np.arange(0,t,dt); 
        self.y_n=self.Ampl*x_n%(1/self.f)<(1/self.f)*0.01*pr
        return self.y_n
    def Signal_triang(self,t):
        if t<=0:
            t=self.t
        x_n=np.arange(0,t,1./self.f_0)
        self.y_n=self.Ampl*signal.sawtooth(2*np.pi*self.f*x_n)
        return self.y_n
    def get_sample_n(self,n): 
        return self.y_n[n]
    def Signal_w(self,t):
        if t<=0:
            t=self.t
        x_n=np.arange(0,t,1./self.f_0)
        y_n=np.exp((complex(-(1/2),self.f))*x_n)
        self.y_n=np.angle(y_n)*self.Ampl/3
        return self.y_n
    def generator(self, t): 
        x_n=np.arange(self.x_n[len(self.x_n)-1],self.x_n[len(self.x_n)-1]+t,1./self.f_0)
        for i in range(len(x_n)):   
            yield (self.Ampl*np.cos(x_n[i]*self.f))
    def get_sample_time(self,t): 
        print(len(self.y_n))
        print(t*self.f_0)
        return self.y_n[t*self.f_0]            

