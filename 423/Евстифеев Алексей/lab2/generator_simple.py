import matplotlib.pyplot as plt
import numpy as np
import math

class Generator_simple():
    
    def __init__(self, frequency, sampling_frequency, duration, amplitude):
        
        self.frequency = frequency
        self.sampling_frequency = sampling_frequency
        self.amplitude = amplitude
        self.time = np.arange(0, duration + 1, 1 / sampling_frequency)
        self.signal = [0]

    def garmonic_signal(self):
        
        self.signal = np.zeros(len(self.time))
        for i in range(len(self.time)):
            self.signal[i] = self.amplitude * np.cos(self.frequency * self.time[i])
            
    def triangular_signal(self):   
        
        self.signal = np.zeros(len(self.time))
        for i in range(len(self.time)):
            self.signal[i] = self.amplitude * math.asin(np.sin(self.time[i]))
    
    def pwm_signal(self):   
        
        self.signal = np.zeros(len(self.time))
        for i in range(len(self.time)):
            s = 0
            s += np.sin((2 * i + 1) * self.frequency * self.time[i])
            self.signal[i] = (4 * self.amplitude / np.pi) * s
        pass
    
    def saw_signal(self):
        
        self.signal = np.zeros(len(self.time))
        for i in range(len(self.time)):
            s = 0
            s += ((-1)**(i + 1)) * (1 / (i+1)) * np.sin(i * self.frequency * self.time[i])
            self.signal[i] = (2 * self.amplitude / np.pi) * s
        pass
    
    def full_signal(self):
        
        if self.signal[len(self.signal) - 1] != 0:
            plt.plot(self.time, self.signal)
            plt.show()
        return self.signal
    
    def part_of_the_signal(self, input_time):
        
        time = np.arange(0, input_time, 1 / self.sampling_frequency)
        
        if self.signal[len(self.signal) - 1] != 0:
            signal = self.signal[:len(time)]
            plt.plot(time, signal)
            plt.show()
            return signal
    
    def generator_func(self, sample_length):
        
        sample_length = np.arange(sample_length, sample_length * 2, 1)
        for i in range(sample_length):
            signal = self.signal[i]
        plt.plot(sample_length, signal)
        plt.show()
        yield signal