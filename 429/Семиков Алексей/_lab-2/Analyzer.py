import numpy as np
import matplotlib.pyplot as plt
import scipy as sp

class Analyzer():
    
    def __init__(self, signal, time):
        
        ''' Принимает аргументы: '''
        
        self.signal = signal
        self.time = time
        self.max_signal = 0
        self.min_signal = 0
        self.razmah = 0

    def create_fourier_spectrum(self):
        
        ''' Создает спект Фурье сигнала '''
        
        fig, axs = plt.subplots(1, 2)
        n_bins = len(self.signal)
        axs[0].hist(self.signal['sepal length (cm)'], bins=n_bins)
        axs[0].set_title('sepal length')
        axs[1].hist(self.signal['petal length (cm)'], bins=n_bins)
        axs[1].set_title('petal length')
        
        
        print('Create Fourier spectrum: Done!')
        pass

    def сounting_characteristics(self):
        
        ''' Подсчет дисперсии, среднего, медианного, минимально и максимального
        значения, размах сигнала '''
        
        self.max_signal = max(self.signal)
        self.min_signal = min(self.signal)
        
        self.razmah = abs(self.max_signal) + abs(self.min_signal)
        
        
        print('Максимальное значение сигнала:', self.max_signal)
        print('Минимальное значение сигнала:', self.min_signal)
        print('Размах сигнала:', self.razmah)
        print('Counting characteristics: Done!')
        pass
    
    def inverse_fourier_transform(self):
        
        ''' Обратное преобразование Фурье '''
        
        fig, axs = plt.subplots(1, 2)
        n_bins = len(self.signal)
        axs[0].hist(self.signal['sepal length (cm)'], bins=n_bins)
        axs[0].set_title('sepal length')
        axs[1].hist(self.signal['petal length (cm)'], bins=n_bins)
        axs[1].set_title('petal length')
        
        print('Inverse Fourier transform: Done!')
        pass