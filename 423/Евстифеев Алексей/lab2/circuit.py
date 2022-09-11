import matplotlib.pyplot as plt
import numpy as np
import scipy.signal

class Circuit():
    
    def __init__(self, signal, time):

        self.signal = signal
        self.time = time
        self.signal_tmp = []
    
    def bypass(self):

        final_signal = self.signal
        return final_signal
    
    def sawtooth_convolution(self):
        
        sawtooth = []
        x = np.arange(0, self.time, 1 / 8)
        saw = np.angle(np.exp((complex(-0.5,8) * x)))
        sawtooth.append(self.signal)
        sawtooth.append(self.signal * saw)
        print(sawtooth)
    
    def buffer(self, input_time = 0):
        
        if input_time != 0:
            self.signal_tmp = np.zeros(input_time)
            self.signal_tmp = self.signal[:input_time]
        if input_time == 0:
            self.signal_tmp = self.signal
    
    def full_signal(self):
        
        plt.plot(self.time, self.signal)
        plt.show()
        return self.signal
    
    def return_yield(self):
        
        plt.plot(self.time, self.signal)
        plt.show()  
        yield self.signal