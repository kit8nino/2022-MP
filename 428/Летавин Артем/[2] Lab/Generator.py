import numpy as np
from scipy import signal



class Generator():  
    
    
    
    
    def __init__(self, f, f_dis, t, a):  
       self.f = f
       self.f_dis = f_dis
       self.t = t
       self.a = a
       self.count = 0
       
     
    
    def CreateSignal_treug(self, t):
        if t <= 0:
            t = self.t
        
        xn = np.arange(0, t, 1. / self.f_dis)
        self.yn = self.a * signal.sawtooth(2 * np.pi * self.f * xn)
        
        return self.yn
    
    def CreateSignal_SHIM(self, t, percen_cycles):
        if t <= 0:
            t = self.t
            
                     
        percent = percen_cycles

        dt = 1 / self.f_dis

        xn = np.arange(0, t, dt); 
        self.yn = self.a * xn % (1 / self.f)<(1 / self.f) * percent / 100 
        
        
        return self.yn
    
    def CreateSignal_saw(self, t):
        if t <= 0:
            t = self.t
        
        xn = np.arange(0, t, 1 / self.f_dis)
        yn = np.exp((complex(-0.5,self.f)) * xn)
        self.yn = np.angle(yn) * self.a / 3
        
        return self.yn
    
    def get_sample_n(self, n): 
        return self.yn[n]

    def get_sample_t(self, t): 
        print(len(self.yn))
        print(t * self.f_dis)
        return self.yn[t * self.f_dis]
    
    def signal_harm_generator(self, t):
        self.xn = np.arange(0, t, 1. / self.f_dis)
        for i in range(len(self.xn)):
            yield (self.a * np.cos(self.xn[i] * self.f))
    
   
    def generator(self, t): 
        xn = np.arange(self.xn[len(self.xn) - 1], self.xn[len(self.xn) - 1] + t, 1. / self.f_dis)
        for i in range(len(xn)):   
            yield (self.a * np.cos(xn[i] * self.f))




