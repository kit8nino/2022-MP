import numpy as np
from simple_signal_generator import simple_signal_generator

class AMS(simple_signal_generator):
    def __init__(self,f,fd,t,A):
        simple_signal_generator.__init__(self,f,fd,t,A)
            
    def create_eveloping(self, A, f):
        
        eveloping = np.zeros(len(self.time))
        for i in range(len(self.time)):    
            eveloping[i] = A * np.sin(f * self.time[i])
        return eveloping

    def create_modulated_signal(self, A, f): 
        
    
        eveloping = self.create_eveloping(A, f)
        
        for i in range(len(self.time)):
            self.signal[i] = A * (1 + (self.A / A) * self.signal[i]) * eveloping[i]