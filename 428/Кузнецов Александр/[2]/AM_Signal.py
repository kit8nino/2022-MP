import numpy as np
from Generator import Generator

class AM_Signal(Generator): 
    
    
    def __init__(self, frequency, yn, t, sampling_rate, a):  
        self.xn = np.arange(0, t, 1 / sampling_rate)
        self.frequency = frequency / 20  
        self.A0 = 2
        self.k = 1
        self.F0 = 10
        self.yn = np.array(yn)
        self.sampling_rate = sampling_rate
        self.a = a
       
    
    def get_f(self, const):
        self.frequency = self.frequency / const
    
    
    def envelope(self):
        self.save_yn = self.yn
        self.yn = (self.A0 + self.k * self.yn) * np.cos(self.f * self.xn + self.F0 * np.pi)
        return self.yn
    
  
    def generator(self, t): 
        xn = np.arange(self.xn[len(self.xn) - 1], self.xn[len(self.xn) - 1] + t, 1. / self.sampling_rate)
        
        for i in xn:
            if self.xn[len(self.xn) - 1] + t >= i:
                yield (self.A0 + self.k * self.save_yn) * np.cos(self.f * i + self.F0 * np.pi) 