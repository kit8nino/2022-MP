import numpy as np
from scipy import signal
import matplotlib.pyplot as plt


class SignalChain:
    """
    Класс цепи: работает как с сигналом в виде массива, так и с последовательно приходящими выборками
    """

    def __init__(self, signal, duration):
        """
        Конструктор
        :param signal: сигнал в виде массива
        :param duration: длительность в секундах
        """
        self.signal = signal
        self.duration = duration
        self.signal_temp = []

    def skip_signal_no_changes(self):
        """
        Пропуск сигнала без изменений (bypass)
        """
        return self.signal

    def filter_butter(self):
        """
        Преобразование сигнала через фильтр Баттерворта с частотой среза (по умолчанию 0.4) и
        заданного порядка N (по умолчанию 4)
        """
        butter = []

        sos = signal.butter(4, 0.4, 'hp', fs=1000, output='sos')
        butter = signal.sosfilt(sos, self.signal)
        if butter[len(butter) - 1] != 0:
            plt.plot(self.duration, butter)
            plt.show()

        return butter

    def storage(self, signal_duration):
        """
        Хранить входной и выходной сигналы в буфере (заполние массива), по умолчанию - без ограничения размера (весь),
        но с возможностью этот размер задать (хранить только последние пришедшие и ушедшие);
        :param self:
        :param signal_duration: длительность сигнала
        """
        if signal_duration == 0:
            self.signal_temp = self.signal

        if signal_duration != 0:
            self.signal_temp = np.zeros(signal_duration)
            self.signal_temp = self.signal[:signal_duration]

    def get_signal(self):
        """
        Возвращает сигнал полным массивом
        """
        plt.plot(self.duration, self.signal)
        plt.show()

        return self.signal

    def yield_signal(self):
        """
        Возвращает сигнал генератором yield
        """
        plt.plot(self.duration, self.signal)
        plt.show()

        yield self.signal
