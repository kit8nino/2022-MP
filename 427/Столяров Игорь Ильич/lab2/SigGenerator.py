# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 12:03:36 2022

@author: Игорь
"""

import numpy as np
import math as m
import matplotlib.pyplot as plt

class SimpleSignalGenerator:

    def __init__(self, frequency, discrete_frequency, time_in_sec, amplitude):

        ''' Принимает аргументы: частоту, частоту дискретизации, длительность в
        секундах, амплитуду '''

        self.frequency = frequency
        self.discrete_frequency = discrete_frequency
        self.amplitude = amplitude
        self.time = np.arange(((-1)*time_in_sec)//2, (time_in_sec + 1)//2, 1 / discrete_frequency)
        self.signal = [0]

    def create_garmonic_signal(self):

        ''' Построение гармонического колебания '''

        self.signal = np.zeros(len(self.time))
        for i in range(len(self.time)):
            self.signal[i] = self.amplitude * np.cos(self.frequency * self.time[i] * m.pi)

        print("Garmonic signal: created")

    def create_triangular_signal(self):

        ''' Построение треугольного сигнала '''    

        self.signal = np.zeros(len(self.time))
        for i in range(len(self.time)):
            self.signal[i] = self.amplitude * m.asin(np.sin(self.frequency * self.time[i] * m.pi))

        print("Trengular signal: created")

    def create_pulse_width_modulation(self):

        ''' Построение ШИМ сигнала '''    

        self.signal = np.zeros(len(self.time))
        for i in range(len(self.time)):
            summ = 0
            for j in range(1,7):
                summ += np.sin((2 * j + 1) * self.frequency * self.time[i] * m.pi)
            self.signal[i] = (4 * self.amplitude / np.pi) * summ
        print("Pulse signal: created")    
        pass

    def create_signal_sawtooth(self):

        ''' Построение сигнала пилы '''

        self.signal = np.zeros(len(self.time))
        for i in range(len(self.time)):
            summ = 0
            for j in range(1,7):
                summ += ((-1)**(j + 1)) * (1 / (j+1)) * np.sin(j * self.frequency * self.time[i] * m.pi)
            self.signal[i] = (2 * self.amplitude / np.pi) * summ
        print("Sawtooth signal: created")    
        pass

    def return_the_signal(self):

        ''' Возвращает весь сигнал '''

        if self.signal[len(self.signal) - 1] != 0:
            plt.plot(self.time, self.signal)
            plt.show()

        print("Full signal: returned")
        return self.signal

    def return_the_selection(self, entered_time):

        ''' Возвращает часть сигнала '''

        time = np.arange(0, entered_time, 1 / self.frequency_diskret)

        if self.signal[len(self.signal) - 1] != 0:
            signal = self.signal[:len(time)]
            plt.plot(time, signal)
            plt.show()
            print("Part of the signal: returned") 
            return signal

    def next_selection(self, lenght_selection):

        ''' Функция генератор, возвращает следующую выборку '''

        lenght_selection = np.arange(lenght_selection, lenght_selection * 2, 1)
        for i in range(lenght_selection):
            signal = self.signal[i]
        plt.plot(lenght_selection, signal)
        plt.show()

        print("Next selection: returned") 
        yield 