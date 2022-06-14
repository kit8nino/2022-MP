from typing import Dict

from scipy.fftpack import fft
import matplotlib.pyplot as plt


class Analyzat_signal():

    def __init__(self, signal: Dict[float, float], label: str = "Input signal"):
        self.X = [x.real for x in signal.keys()]
        self.Y = [y.real for y in signal.values()]
        self.math_waiting = lambda x: sum(x) / len(x)
        self.plotHorizontaLine = lambda y, labelLine: plt.plot([self.X[0] , self.X[-1]] , [y]*2 ,'--' , label = labelLine)
        plt.plot(self.X, self.Y, label=label)

    def add_Fourier_spectrum(self, label: str = "fft"):
        Y_fft = abs(fft(self.Y))
        plt.plot(self.X, Y_fft, '--', label=label)

    def add_midl_Value(self):
        midlValue = self.math_waiting(self.Y)
        self.plotHorizontaLine(midlValue , "midl Value")

    def add_median_Value(self):
        sortValueY = sorted(self.Y)
        median_Value = 0
        if len(sortValueY) % 2 == 0:
            median_Value = sortValueY[len(sortValueY)//2]
        else:
            median_Value = sortValueY[(len(sortValueY)+1) // 2]
        self.plotHorizontaLine(median_Value , "median Value")

    def add_max_Value(self):
        self.plotHorizontaLine(max(self.Y) , "max Value")

    def add_min_Value(self):
        self.plotHorizontaLine(min(self.Y) , "min Value")

    def add_Dispersion(self):
        math_waiting_Y = self.math_waiting(self.Y)
        dispersion = self.math_waiting( [ (y - math_waiting_Y)**2 for y in self.Y ])
        self.plotHorizontaLine(dispersion , "dispersion")

    def show(self):
        plt.grid()
        plt.legend()
        plt.show()