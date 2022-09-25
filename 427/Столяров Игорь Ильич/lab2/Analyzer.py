# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 12:06:39 2022

@author: Игорь
"""

import numpy as np
from numpy.fft import fft
import matplotlib.pyplot as plt

class Analyzer():

    def __init__(self, signal, time):

        ''' Принимает аргументы: '''

        self.signal = signal
        self.time = time
        self.max_signal = 0
        self.min_signal = 0
        self.sweep = 0
        self.spect = 0
        self.frq = 0

    def create_spectrum(self):

        ''' Создает спектр Фурье сигнала '''

        n = len(self.signal) 
        k = np.arange(n)
        T = n
        frq = k/T 
        frq = frq[range(n//2)] 

        Y = fft(self.signal)/n 
        Y = Y[range(n//2)]
        plt.plot(frq, abs(Y), 'r') 
        plt.show()
        self.spect = Y

        self.frq = frq


        print("Create Fourier spectrum: created")
        pass

    def сounting_characteristics(self):

        ''' Подсчет дисперсии, среднего, медианного, минимально и максимального
        значения, размах сигнала '''

        self.max_signal = max(self.signal)
        self.min_signal = min(self.signal)

        self.sweep = abs(self.max_signal) + abs(self.min_signal)


        print("Максимальное значение сигнала:", self.max_signal)
        print("Минимальное значение сигнала:", self.min_signal)
        print("Размах сигнала:", self.sweep)
        print("Counting characteristics: counted")
        pass

    def inverse_fourier_transform(self):

        ''' Обратное преобразование Фурье '''

        fig, axs = plt.subplots(1, 2)
        n_bins = len(self.signal)
        axs[0].hist(self.signal["sepal length (cm)"], bins = n_bins)
        axs[0].set_title("sepal length")
        axs[1].hist(self.signal["petal length (cm)"], bins = n_bins)
        axs[1].set_title("petal length")

        print("Inverse Fourier transform: transformed")
        pass 