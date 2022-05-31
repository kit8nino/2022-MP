import numpy as np
import math as m
import matplotlib.pyplot as plt
from scipy import signal

class SignalGenerator:
    
    def __init__(self, frequency, frequency_diskret, time_in_sec, amplitude,choose):
    
        self.frequency = frequency
        self.frequency_diskret = frequency_diskret
        self.amplitude = amplitude
        self.time = np.arange(0, time_in_sec + 1, 1 / frequency_diskret)
        self.signal = [0]
        self.choose=choose
        
    def create_garmonic_signal(self):
        
        
        self.signal = np.zeros(len(self.time))
        for i in range(len(self.time)):
            self.signal[i] = self.amplitude * np.cos(self.frequency * self.time[i])
        
        return self.signal
    
    def create_triangl_signal(self):
    
        
        self.signal = np.zeros(len(self.time))
        for i in range(len(self.time)):
            self.signal[i] = self.amplitude * m.asin(np.sin(self.time[i]))
        
        return self.signal
    
    def create_SHIM_signal(self):
        self.signal = np.zeros(len(self.time))
        self.signal=self.amplitude*signal.square( self.frequency *self.time,duty=0.5) 
        return self.signal
    
    def create_saw_signal(self):
        
        self.signal = np.zeros(len(self.time))
        self.signal=self.amplitude*signal.sawtooth(2 * np.pi * self.frequency *self.time)                                             
        return self.signal
    
    
    def return_the_signal(self):
        
        if self.signal[len(self.signal) - 1] != 0:
            
                plt.title(self.choose)
                plt.xlabel("Время в секундах")
                plt.ylabel('A(w)')
                plt.plot(self.time, self.signal)
                plt.show()
        
        return self.signal
   
    def return_the_piece(self, entered_time):
        
        time = np.arange(0, entered_time, 1 / self.frequency_diskret)
        if self.signal[len(self.signal) - 1] != 0:
            signal = self.signal[:len(time)]
            plt.title('График выборки сигнала')
            plt.plot(time, signal)
            plt.show()
            return signal
    
    def next_selection(self, lenght_selection):
        
        lenght_selection = np.arange(lenght_selection, lenght_selection * 2, 1)
        for i in range(lenght_selection):
            signal = self.signal[i]
        #self.choose='График мод сигнала по выборке' 
        plt.title('Следующая выборка')
        plt.plot(lenght_selection, signal)
        plt.show()
        yield signal
