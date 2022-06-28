# Класс анализатора
import matplotlib.pyplot as plt
from numpy.fft import fft
import numpy as np

class Analyzer():
     def __init__(self, yn, t, f_dis):
        self.f_dis = f_dis
        self.yn = yn
        self.xn = np.arange(0, t, 1. / self.f_dis)
        self.spect = 0
        self.frq = 0
        
     def Graph(self, count):
        self.count = count
        plt.figure(self.count)
        plt.subplot(2, 1, 1)
        plt.plot(self.xn, self.yn)
        plt.show()   
        
     def Spectr(self):
        y = self.yn
        n = len(y) 
        k = np.arange(n)
        T = n
        frq = k/T 
        frq = frq[range(n//2)] 

        Y = fft(y)/n 
        Y = Y[range(n//2)]
        plt.subplot(2, 1, 2)
        plt.plot(frq,abs(Y),'r') 
        self.spect = Y
 
        self.frq = frq

