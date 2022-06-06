import numpy as np
from scipy import signal

class Generator():  

    def __init__(self, frequency, freq_dis, time, amplitude):  
       self.f = frequency
       self.f_dis = freq_dis
       self.t = time
       self.a = amplitude
       self.count = 0
       
  
    def Make_triangle(self, time):
        if time <= 0:
            time = self.time
        xn = np.arange(0, time, 1. / self.f_dis)
        self.yn = self.a * signal.sawtooth(2 * np.pi * self.f * xn)
        return self.yn
    
    def Make_SHIM(self, time, percen_cycles):
        if time <= 0:
            time = self.t
        percent = percen_cycles
        dt = 1 / self.f_dis
        xn = np.arange(0, time, dt); 
        self.yn = self.a * xn % (1 / self.f)<(1 / self.f) * percent / 100 
        return self.yn
    
    def Make_saw(self, time):
        if time <= 0:
            time = self.t
        xn = np.arange(0, time, 1 / self.f_dis)
        yn = np.exp((complex(-0.5,self.f)) * xn)
        self.yn = np.angle(yn) * self.a / 3
        return self.yn
    
    def get_signal_n(self, n): 
        return self.yn[n]

    def get_signal_t(self, time): 
        print(len(self.yn))
        print(time * self.f_dis)
        return self.yn[time * self.f_dis]
    
    def Make_harm(self, time):
        self.xn = np.arange(0, time, 1. / self.f_dis)
        for i in range(len(self.xn)):
            yield (self.a * np.cos(self.xn[i] * self.f))
    
   
    def generator(self, time): 
        xn = np.arange(self.xn[len(self.xn) - 1], self.xn[len(self.xn) - 1] + time, 1. / self.f_dis)
        for i in range(len(xn)):   
            yield (self.a * np.cos(xn[i] * self.f))
