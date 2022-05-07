import matplotlib.pyplot as plt
from numpy.fft import rfft, rfftfreq, fft, ifft
import numpy as np
import math as m


class Circuit():
    
    def __init__(self, yn, t, f_dis):
        
        self.a = 1
        self.yn = yn
        self.t = t
        self.f_dis = f_dis
        self.buffer = list()
        self.signal = list()
    
    def convolution(self):
        
        xn = np.arange(0, self.t, 1 / self.f_dis)
        saw = np.angle(np.exp((complex(-0.5,8) * xn)))
        self.buffer.append(self.yn)
        self.buffer.append(self.yn * saw)
        self.signal = self.yn * saw
        
        return(self.yn * saw)
        
    def Get_Buffer(self, i): # 0 входной 1 выходной
        if i < 0:
            return self.bufferх[0]
        return self.buffer[1]
    
    def No_Change(self):
        return self.yn
    
    def Return_Array(self): # вернуть полный массив сигнала
        return self.buffer[1]
    
    def Return_Generator(self): # вернуть генератором
        for i in self.buffer[0]:
            yield i
            
            