import numpy as np
import matplotlib.pyplot as plt


class simple_signal_generator:
    def __init__(self,f,fd,t,A):
        self.f=f
        self.fs=fd
        self.t=t
        self.A=A
        self.time=np.arange(0,t+1,1/fd)       
        self.signal=[0]
        
    def generator_sin(self):
        self.signal = np.zeros(len(self.time))
        for i in range(len(self.time)):
            self.signal[i] = self.A * np.cos(self.f * self.time[i])
    
    def return_the_signal(self):
    
        
        if self.signal[len(self.signal) - 1] != 0:
            plt.plot(self.time, self.signal)
            plt.show()
        
        return self.signal
