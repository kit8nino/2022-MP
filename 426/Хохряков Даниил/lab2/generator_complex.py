from generator_simple import Generator_simple
import matplotlib.pyplot as plt
import numpy as np

class Generator_complex(Generator_simple):
    
    def __init__(self, frequency, sampling_frequency, duration, amplitude):
        
        Generator_simple.__init__(self, frequency, sampling_frequency, duration, amplitude)
        
    def envelope(self, amplitude, frequency):
        
        envelope = np.zeros(len(self.time))
        for i in range(len(self.time)):    
            envelope[i] = amplitude * np.cos(frequency * self.time[i])
        return envelope
    
    def am_signal(self, amplitude, frequency):
    
        envelope = self.envelope(amplitude, frequency)
        
        for i in range(len(self.time)):
            self.signal[i] = amplitude * (1 + (self.amplitude / amplitude) * self.signal[i]) * envelope[i]