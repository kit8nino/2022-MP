#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import scipy.signal
import numpy as np
import math as m
import matplotlib.pyplot as plt
from numpy.fft import rfft, rfftfreq, fft, ifft

class Circut():
    def __init__(self, y_n,t,f_0):
        self.a=1
        self.y_n=y_n
        self.t=t
        self.f_0=f_0
        self.buf=list()
        self.sig=list()
    def convol(self):
        x_n=np.arange(0,self.t,1./self.f_0)
        w=np.angle(np.exp((complex(-(1/2),8)*x_n)))
        self.buf.append(self.y_n)
        self.buf.append(self.y_n*w)
        self.sig=self.y_n*w
        return(self.y_n*w)
    def Get_Buf(self,a):
        if a<0:
            return self.bufх[0]
        return self.buf[1]
    def Return_Ar(self):
        return self.buf[1]
    def No_Change(self):
        return self.y_n
    def Return_Gener(self):
        for i in self.buf[0]:
            yield 
