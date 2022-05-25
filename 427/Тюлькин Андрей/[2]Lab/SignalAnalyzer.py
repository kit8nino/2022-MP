import numpy as np
from numpy.fft import fft
import matplotlib.pyplot as plt


class SignalAnalyzer:
    """
    Класс анализатора строит график по полученному временнОму представлению сигнала
    """

    def __init__(self, signal, duration):
        """
        Конструктор
        :param signal: сигнал
        :param duration: время
        """
        self.signal = signal
        self.duration = duration
        self.max_signal = 0
        self.min_signal = 0
        self.scope = 0
        self.spect = 0
        self.frq = 0

    def build_fourier_spectrum(self):
        """
        Cтроит спектр Фурье
        """
        n = len(self.signal)
        k = np.arange(n)
        T = n
        frq = k / T
        frq = frq[range(n // 2)]

        Y = fft(self.signal) / n
        Y = Y[range(n // 2)]
        plt.plot(frq, abs(Y), 'r')
        plt.show()
        self.spect = Y

        self.frq = frq

    def count_statistics_data(self):
        """
        :return: дисперсию, среднее, медианное, минимальное и максимальное значения, размах сигнала
        """
        self.max_signal = max(self.signal)
        self.min_signal = min(self.signal)
        self.scope = abs(self.max_signal) + abs(self.min_signal)

    def transform_reverse_fourier_spectrum(self):
        """
        Cтроит примерный (прогнозируемый) сигнал с помощью обратного преобразования Фурье, используя первые несколько
        максимальных гармоник (частот) спектра Фурье (по умолчанию - 5, но можно задать любое).
        """
        fig, axs = plt.subplots(1, 2)
        n_bins = len(self.signal)
        axs[0].hist(self.signal['sepal length (cm)'], bins=n_bins)
        axs[0].set_title('sepal length')
        axs[1].hist(self.signal['petal length (cm)'], bins=n_bins)
        axs[1].set_title('petal length')
