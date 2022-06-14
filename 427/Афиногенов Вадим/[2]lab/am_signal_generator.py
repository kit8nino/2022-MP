import numpy as np
from signal_generator import signal_generator

class am_signal(signal_generator):
    
    def __init__(self, frequency, frequency_discret, time_in_sec, amplitude,choose):
        signal_generator.__init__(self, frequency, frequency_discret, time_in_sec, amplitude,choose)
    
    # огибающая        
    def create_eveloping(self, amplitude, frequency):
        eveloping = np.zeros(len(self.time))
        for i in range(len(self.time)):    
            eveloping[i] = amplitude * np.cos(frequency * self.time[i])
        return eveloping
    
    def create_modulated_signal(self, amplitude, frequency): 
        self.choose='График модулирующего сигнала'
        eveloping = self.create_eveloping(amplitude, frequency)
        for i in range(len(self.time)):
            self.signal[i] = amplitude * (1 + (self.amplitude / amplitude) * self.signal[i]) * eveloping[i] 
            