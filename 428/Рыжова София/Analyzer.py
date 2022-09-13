#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import matplotlib.pyplot as plt
import numpy as np
from numpy.fft import fft

class Analyzer():
    def __init__(self,y_n,t,f_0):
        self.f_0=f_0
        self.y_n=y_n
        self.x_n=np.arange(0,t,1./self.f_0)
        self.spect=0
        self.frq=0
    def Graph(self,count):
        self.count=count
        plt.figure(self.count)
        plt.subplot(2,1,1)
        plt.plot(self.x_n, self.y_n)
        plt.show()   
    def Spectr(self):
        y=self.y_n
        p=len(y) 
        k=np.arange(p)
        T=p
        frq=k/T 
        frq=frq[range(p//2)] 
        Y=fft(y)/p 
        Y=Y[range(p//2)]
        plt.subplot(2,1,2)
        plt.plot(frq,abs(Y),'r') 
        self.spect=Y
        self.frq=frq
    def Disper(self,ch):
        v= np.v(self.y_n) 
        if ch==1:
            plt.figure(self.count)
            plt.subplot(2,1,1)
            plt.plot(self.x_n,v*np.ones(len(self.x_n)),label='dispersion')
            plt.legend()
        return v
    def Average(self,ch):
        aver=sum(self.y_n)/len(self.y_n) 
        if ch==1:
            plt.figure(self.count)
            plt.subplot(2,1,1)
            plt.plot(self.x_n,aver*np.ones(len(self.x_n)),label='average')
            plt.legend()
        return aver
    def Median(self,ch):
        j=len(self.y_n)
        index=j//2
        if j%2:
            median=sorted(self.y_n)[index]
        else:
            median=sum(sorted(self.y_n)[index-1:index+1])*0.5
        if ch==1:
            plt.figure(self.count)
            plt.subplot(2,1,1)
            plt.plot(self.x_n,median*np.ones(len(self.x_n)),label='median')
            plt.legend()
        return median
    def Max(self,ch):
        maxim=max(self.y_n)
        if ch==1:
            plt.figure(self.count)
            plt.subplot(2, 1, 1)
            plt.plot(self.x_n,maxim*np.ones(len(self.x_n)),label='max')
            plt.legend()
        return maxim
    def Min(self,ch):
        minim=min(self.y_n) 
        if ch==1:
            plt.figure(self.count)
            plt.subplot(2, 1, 1)
            plt.plot(self.x_n, minim*np.ones(len(self.x_n)), label='min')
            plt.legend()
        return minim
    def Scope(self,ch):
        minim=min(self.y_n)
        maxim=max(self.y_n)
        scope=abs(maxim)+abs(minim)
        if ch==1:
            plt.figure(self.count)
            plt.subplot(2, 1, 1)
            plt.plot(self.x_n,scope*np.ones(len(self.x_n)),label='scope')
            plt.legend()
    def Reverse_Fourier(self,ch):
        y=np.fft.ifft(self.spect)*100
        if ch==1:
            plt.figure(self.count+10)
            plt.subplot(2,1,1)
            plt.plot(self.frq,y.real,label='real')
            plt.plot(self.frq,y.imag,'--',label='imaginary')
            plt.legend()
            plt.show()
        return y
