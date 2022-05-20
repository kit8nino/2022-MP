import scipy.signal
import numpy as np
import matplotlib.pyplot as plt

class Circuit():
    
    def __init__(self, signal, time):

        self.signal = signal
        self.time = time
        self.signal_temp = []
    
    def without_changes(self):

        final_signal = self.signal
        
        print('Signal transmission without changes: Done!')
        return final_signal
    
    def bessel_filter(self):
        
        bessel = []
        bessel.append(1)
        bessel.append(self.signal[1] + 1)
        
        for i in range(2, len(self.signal) - 1):
            bessel.append((2 * len(self.signal) - 1) * bessel[i - 1] + self.signal[i]**2 * bessel[i - 2])
        
        print(bessel)
        
        print('Bassel Filter: Done!')
    
    def storage(self, entered_time = 0):
        
        if entered_time != 0:
            self.signal_temp = np.zeros(entered_time)
            self.signal_temp = self.signal[:entered_time]
            
        if entered_time == 0:
            self.signal_temp = self.signal

        print('Clipboard storage: Done!')
    
    def full_signal(self):
        
        plt.plot(self.time, self.signal)
        plt.show()
        return self.signal
    
    def return_yield(self):
        
        plt.plot(self.time, self.signal)
        plt.show()  
        yield self.signal