import numpy as np
import matplotlib.pyplot as plt

class Chains():
    
    def __init__(self, signal, time):
        

        self.signal = signal
        self.time = time
        self.signal_temp = []
    
    def signal_transmission_without_changes(self):
            

        signal_end = self.signal # конечный вид сигнала, после прохождения цепи
        
        print('Signal transmission without changes: Done!')
        return signal_end
    
    def bessel_filter(self): # Прохождение сигнала через фильтр Бесселя 
        #Параметры по умолчанию: частота среза = 0.4, N = 4
        
        bessel = []
        
        bessel.append(1)
        bessel.append(self.signal[1] + 1)
        
        for i in range(2, len(self.signal) - 1):
            bessel.append((2 * len(self.signal) - 1) * bessel[i - 1] + self.signal[i]**2 * bessel[i - 2])
        
        print(bessel)
        
        print('Bassel Filter: Done!')
    
    def clipboard_storage(self, entered_time = 0): # Хранит сигнал или его часть в буфере обмена 
    
        if entered_time == 0:
            self.signal_temp = self.signal
        
        if entered_time != 0:
            self.signal_temp = np.zeros(entered_time)
            self.signal_temp = self.signal[:entered_time]
    
        print('Clipboard storage: Done!')
    
    def return_full_signal(self): #Возвращает полный сигнал 
            
        plt.plot(self.time, self.signal)
        plt.show()
        
        print('Return full signal: Done!')
        return self.signal
    
    def return_yield(self):
        
        plt.plot(self.time, self.signal)
        plt.show()
        
        print('Return yield: Done!')    
        yield self.signal