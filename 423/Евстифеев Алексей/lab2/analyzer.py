import matplotlib.pyplot as plt
import numpy as np

class Analyzer():
    
    
    def __init__(self, signal, time):
        
        self.signal = signal
        self.time = time
        self.max_signal = 0
        self.min_signal = 0
        self.range = 0

    def spectrum(self):
        
        fig, axs = plt.subplots(1, 2)
        length = len(self.signal)
        
        axs[0].hist(self.signal['sepal length'], bins=length)
        axs[0].set_title('sepal length')
        axs[1].hist(self.signal['petal length'], bins=length)
        axs[1].set_title('petal length')
        pass

    def characteristics(self):
        
        self.max_signal = max(self.signal)
        self.min_signal = min(self.signal)
        self.range = abs(self.max_signal) + abs(self.min_signal)
              
        print('Maximum signal value:', self.max_signal)
        print('Minimum signal value:', self.min_signal)
        print('The signal range:', self.range)
        pass
    
    def inverse_Fourier(self):
        
        fig, axs = plt.subplots(1, 2)
        length = len(self.signal)
        axs[0].hist(self.signal['sepal length'], bins=length)
        axs[1].hist(self.signal['petal length'], bins=length)
        pass