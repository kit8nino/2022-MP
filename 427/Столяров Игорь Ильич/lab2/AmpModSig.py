# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 12:05:04 2022

@author: Игорь
"""
import numpy as np
import math as m
import matplotlib.pyplot as plt
from SigGenerator import SimpleSignalGenerator

class AmplitudeModulatedSignal(SimpleSignalGenerator):

    def __init__(self, frequency, frequency_discret, time_in_sec, amplitude):
        SimpleSignalGenerator.__init__(self, frequency, frequency_discret, time_in_sec, amplitude)
        self.sig = [0]

    ''' Методы возвращения полного сигнала и его выборки реализованы
        в классе родителе '''

    def create_eveloping(self, amplitude, frequency):

        ''' Создает огибающую для модуляции сигнала '''

        eveloping = np.zeros(len(self.time))
        for i in range(len(self.time)):    
            eveloping[i] = amplitude * np.cos(frequency * self.time[i] * m.pi )
        return eveloping

    def create_modulated_signal(self, amplitude, frequency): 
        ''' Создает амплитудно-модулированный сигнал '''
        eveloping = self.create_eveloping(amplitude, frequency)
        for i in range(len(self.time)):
            self.signal[i] = amplitude * (1 + (self.amplitude / amplitude) * self.signal[i]) * eveloping[i]
        self.sig = np.zeros(len(self.time))
        for i in range(len(self.time)):
            sig[i] = self.signal[i]
        print('Create the modulated signal: created') 
        