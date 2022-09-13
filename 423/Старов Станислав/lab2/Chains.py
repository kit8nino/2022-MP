import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
class Chains():
    def __init__(self, signal, time):
        # Конструктор цепи принимает: сигнал в виде массива,длительность этого сигнала в секундах
        self.signal = signal
        self.time = time
        self.signal_temp = []
    def signal_transmission_without_changes(self):
        # Прохождение сигнала по цепи без изменений
        signal_end = self.signal # конечный вид сигнала, после прохождения цепи
        print('Передача сигнала без изменений')
        return signal_end
    def butter_filter(self):
        # Прохождение сигнала через фильтр Баттерворта  Параметры по умолчанию: частота среза = 0.4, N = 4
        butter = []
        sos = signal.butter (4, 0.4, 'hp', fs = 1000, output = 'sos')
        butter=signal.sosfilt(sos, self.signal)
        if butter[len(butter) - 1] != 0:
            plt.plot(self.time,butter)
            plt.show()
        print(butter)
        print('Фильтр')
        return butter
    def clipboard_storage(self, entered_time = 0):
        # Хранит сигнал в буфере обмена
        if entered_time == 0:
            self.signal_temp = self.signal
        if entered_time != 0:
            self.signal_temp = np.zeros(entered_time)
            self.signal_temp = self.signal[:entered_time]
        print('Буфер')
    def return_full_signal(self):
        # Возвращает полный сигнал 
        plt.plot(self.time, self.signal)
        plt.show()
        print('Возврат полного сигнала')
        return self.signal
    def return_yield(self):
        # Вернуть полный сигнал генератором yield 
        plt.plot(self.time, self.signal)
        plt.show()
        print('Возврат полного сигнала  генератором yield')    
        yield self.signal 
