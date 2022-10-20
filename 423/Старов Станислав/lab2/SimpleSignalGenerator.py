import numpy as np
import math as m
import matplotlib.pyplot as plt
class SimpleSignalGenerator:
    def __init__(self, frequency, frequency_diskret, time_in_sec, amplitude):
       # Принимает аргументы: частоту, частоту дискретизации, длительность(сек), амплитуду
        self.frequency = frequency
        self.frequency_diskret = frequency_diskret
        self.amplitude = amplitude
        self.time = np.arange(0, time_in_sec + 1, 1 / frequency_diskret)
        self.signal = [0]
    def create_garmonic_signal(self):
        # Построение гармонического колебания 
        self.signal = np.zeros(len(self.time))
        for i in range(len(self.time)):
            self.signal[i] = self.amplitude * np.cos(self.frequency * self.time[i])
        print('Создание гармонического сигнала')
    def create_triangular_signal(self):
        # Построение треугольного сигнала    
        self.signal = np.zeros(len(self.time))
        for i in range(len(self.time)):
            self.signal[i] = self.amplitude * m.asin(np.sin(self.time[i]))
        print('Треугольный сигнал')
    def create_pulse_width_modulation(self):
        # Построение ШИМ сигнала   
        self.signal = np.zeros(len(self.time))
        for i in range(len(self.time)):
            summ = 0
            summ += np.sin((2 * i + 1) * self.frequency * self.time[i])
            self.signal[i] = (4 * self.amplitude / np.pi) * summ
        print('ШИМ сигнал')    
        pass
    def create_signal_saw(self):
        # Построение сигнала пилы
        self.signal = np.zeros(len(self.time))
        for i in range(len(self.time)):
            summ = 0
            summ += ((-1)**(i + 1)) * (1 / (i+1)) * np.sin(i * self.frequency * self.time[i])
            self.signal[i] = (2 * self.amplitude / np.pi) * summ
        print('Сигнал пилы')    
        pass
    def return_the_signal(self):
        # Возвращает весь сигнал 
        if self.signal[len(self.signal) - 1] != 0:
            plt.plot(self.time, self.signal)
            plt.show()
        print('Полный весь сигнал')
        return self.signal
    def return_the_selection(self, entered_time):
        # Возвращает часть сигнала 
        time = np.arange(0, entered_time, 1 / self.frequency_diskret)
        if self.signal[len(self.signal) - 1] != 0:
            signal = self.signal[:len(time)]
            plt.plot(time, signal)
            plt.show()
            print('Часть сигнала') 
            return signal
    def next_selection(self, lenght_selection):
        # Функция генератор, возвращает следующую выборку 
        lenght_selection = np.arange(lenght_selection, lenght_selection * 2, 1)
        for i in range(lenght_selection):
            signal = self.signal[i]
        plt.plot(lenght_selection, signal)
        plt.show()
        print('Генератор, следующая выборка') 
        yield signal
