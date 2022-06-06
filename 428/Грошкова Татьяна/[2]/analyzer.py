import matplotlib.pyplot as plt
import numpy as np
from numpy.fft import fft

class Analyzer():
    def __init__(self,y_new,time,fr_0):
        self.fr_0=fr_0
        self.y_new=y_new
        self.x_new=np.arange(0,time,1./self.fr_0)
        self.spect=0
        self.frq=0
    def Graph(self,count):
        self.count=count
        plt.figure(self.count)
        plt.subplot(2,1,1)
        plt.plot(self.x_new, self.y_new)
        plt.show()   
    def Spectr(self):
        y=self.y_new
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
        v= np.v(self.y_new) 
        if ch==1:
            plt.figure(self.count)
            plt.subplot(2,1,1)
            plt.plot(self.x_new,v*np.ones(len(self.x_new)),label='dispersion')
            plt.legend()
        return v
    def Average(self,ch):
        aver=sum(self.y_new)/len(self.y_new) 
        if ch==1:
            plt.figure(self.count)
            plt.subplot(2,1,1)
            plt.plot(self.x_new,aver*np.ones(len(self.x_new)),label='average')
            plt.legend()
        return aver
    def Median(self,ch):
        j=len(self.y_new)
        index=j//2
        if j%2:
            median=sorted(self.y_new)[index]
        else:
            median=sum(sorted(self.y_new)[index-1:index+1])*0.5
        if ch==1:
            plt.figure(self.count)
            plt.subplot(2,1,1)
            plt.plot(self.x_new,median*np.ones(len(self.x_new)),label='median')
            plt.legend()
        return median
    def Max(self,ch):
        maxim=max(self.y_new)
        if ch==1:
            plt.figure(self.count)
            plt.subplot(2, 1, 1)
            plt.plot(self.x_new,maxim*np.ones(len(self.x_new)),label='max')
            plt.legend()
        return maxim
    def Min(self,ch):
        minim=min(self.y_new) 
        if ch==1:
            plt.figure(self.count)
            plt.subplot(2, 1, 1)
            plt.plot(self.x_new, minim*np.ones(len(self.x_new)), label='min')
            plt.legend()
        return minim
    def Scope(self,ch):
        minim=min(self.y_new)
        maxim=max(self.y_new)
        scope=abs(maxim)+abs(minim)
        if ch==1:
            plt.figure(self.count)
            plt.subplot(2, 1, 1)
            plt.plot(self.x_new,scope*np.ones(len(self.x_new)),label='scope')
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