import scipy.signal
import numpy as np
import math as m
import matplotlib.pyplot as plt
from numpy.fft import rfft, rfftfreq, fft, ifft

class Circut():
    def __init__(self, y_new,time,fr_0):
        self.a=1
        self.y_new=y_new
        self.time=time
        self.fr_0=fr_0
        self.buf=list()
        self.sig=list()
    def convol(self):
        x_new=np.arange(0,self.time,1./self.f_dis)
        w=np.angle(np.exp((complex(-(1/2),8)*x_new)))
        self.buf.append(self.y_new)
        self.buf.append(self.y_new*w)
        self.sig=self.y_new*w
        return(self.y_new*w)
    def Get_Buf(self,a):
        if a<0:
            return self.bufх[0]
        return self.buf[1]
    def Return_Ar(self):
        return self.buf[1]
    def No_Change(self):
        return self.y_new
    def Return_Gener(self):
        for i in self.buf[0]:
            yield 

