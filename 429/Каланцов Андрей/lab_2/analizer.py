from generator import Generator
from scipy.fft import rfft, rfftfreq, irfft
import numpy as np


class Analizer:

    def __init__(self, signal: Generator):
        self.signal = signal
        self.s = []

    def get(self):
        if not self.s:
            self.s = self.signal.get()
        return self.s 

    def var(self):
        ''' Дисперсия '''
        s = self.get()
        return np.var(s)

    def mean(self):
        ''' Среднее значение '''
        s = self.get()
        return np.mean(s)

    def median(self):
        ''' Медианное значение '''
        s = self.get()
        return np.median(s)

    def min(self):
        ''' Минимальное значение '''
        s = self.get()
        return np.min(s)

    def max(self):
        ''' Максимальное значение '''
        s = self.get()
        return np.max(s)

    def scope(self):
        ''' Размах '''
        s = self.get()
        return np.max(s) - np.min(s)

    def plot(self, ax):
        s = self.get()
        n = len(s)
        x = range(n)
        ax.plot(x, s)

        s_min = self.min()
        s_max = self.max()
        s_scope = self.scope()
        s_mean = self.mean()
        s_median = self.median()
        s_var = self.var()

        ax.hlines([s_min, s_max, s_mean], [0, 0, 0], [n-1, n-1, n-1], 
                    linestyles=['dotted', 'dotted', 'dashed'],
                    colors=['gray', 'gray', 'pink'], linewidths=[0.5, 0.5, 0.75])

    def fft(self):
        ''' Спектр Фурье '''
        s = self.get()
        yf = rfft(s)
        xf = rfftfreq(self.signal.total, 1/self.signal.freq)
        return xf, yf

    def plot_fft(self, ax):
        xf, yf = self.fft()
        ax.plot(xf, np.abs(yf))

    
    def plot_rfft(self, ax):
        ''' Обратное преобразование Фурье '''
        xf, yf = self.fft()
        n = len(yf)
        values = sorted([[np.abs(yf[i]), yf[i], xf[i]] for i in range(n)], reverse=True)
        
        for i in range(5, n):
            values[i][1] = 0
        
        values = sorted([[v[2], v[1]] for v in values])
        yf = [v[1] for v in values]
        yf = irfft(yf)
        ax.plot(yf)
