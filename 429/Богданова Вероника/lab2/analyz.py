#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
from numpy.fft import fft
import matplotlib.pyplot as plt
import scipy

class Analyzer():
    
    def __init__(self, signal, time):
        
        self.signal = signal
        self.time = time
        self.max_signal = 0
        self.min_signal = 0
        self.razmah = 0
        self.spect = 0
        self.frq = 0

    def create_spectrum(self):
        
        
        
        n = len(self.signal) 
        k = np.arange(n)
        T = n
        frq = k/T 
        frq = frq[range(n//2)] 

        Y = fft(self.signal)/n 
        Y = Y[range(n//2)]
        plt.title('Спектр сигнала')
        plt.plot(frq,abs(Y),'r') 
        plt.show()
        self.spect = Y
        self.frq = frq
        
        
    def characteristics(self):
        
        self.max_signal = max(self.signal)
        self.min_signal = min(self.signal)
        self.razmah = abs(self.max_signal) + abs(self.min_signal)
        
        print('Максимальное значение сигнала:', self.max_signal)
        print('Минимальное значение сигнала:', self.min_signal)
        print('Размах сигнала:', self.razmah)
    
    def inverse_fourier_transform(self):
        s=scipy.fft.ifft(self.signal)
        plt.title('Обратное преобразование Фурье')
        plt.plot(self.time,s.real,s.imag)
        plt.show()


# In[ ]:




