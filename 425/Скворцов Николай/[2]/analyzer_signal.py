from scipy.fft import rfft, rfftfreq, irfft
import numpy as np
from gen_simple_signal import Generator_simple

class Analyzer():
    print('Signl --> grafical part')
    
    def __init__(self, signall: Generator_simple):
        self.signall = signall
        self.ss = []

    def get(self):
        if not self.ss:
            self.ss = self.signall.get()
        return self.ss 

    def var(self): # Дисперсия
        ss = self.get()
        return np.var(ss)

    def mean(self): # Среднее значение
        ss = self.get()
        return np.mean(ss)

    def median(self): # Медианное значение
        ss = self.get()
        return np.median(ss)

    def min(self): # Минимальное значение 
        ss = self.get()
        return np.min(ss)

    def max(self): # Максимальное значение
        ss = self.get()
        return np.max(ss)

    def scope(self): # Размах 
        ss = self.get()
        return np.max(ss) - np.min(ss)

    def plot(self, axx):
        ss = self.get()
        nn = len(ss)
        xx = range(nn)
        axx.plot(xx, ss)

        s_minn = self.min()
        s_maxx = self.max()
        s_meann = self.mean()
            
        axx.hlines([s_minn, s_maxx, s_meann], [0, 0, 0], [nn-1, nn-1, nn-1], 
                    linestyles=['dotted', 'dotted', 'dashed'],
                    colors=['gray', 'gray', 'pink'], linewidths=[0.5, 0.5, 0.75])

    def fft(self): # Спектр Фурье
        ss = self.get()
        yff = rfft(ss)
        xff = rfftfreq(self.signall.total, 1/self.signall.freq)
        return xff, yff

    def plot_fft(self, axx): # построение спектра Фурье из функции fft(self)
        xff, f = self.fft()
        axx.plot(xff, np.abs(f))

    
    def plot_rfft(self, axx): # Обратное преобразование Фурье
        xff, yff = self.fft()
        nn = len(yff)
        valuess = sorted([[np.abs(yff[i]), yff[i], xff[i]] for i in range(nn)], reverse = True)
        
        for i in range(5, nn):
            valuess[i][1] = 0
        
        valuess = sorted([[v[2], v[1]] for v in valuess])
        yff = [v[1] for v in valuess]
        yff = irfft(yff)
        axx.plot(yff)

