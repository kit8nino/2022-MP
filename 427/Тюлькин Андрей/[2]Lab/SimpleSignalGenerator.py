import numpy as np
import math
import matplotlib.pyplot as plt


class SimpleSignalGenerator:
    """
        Класс генератора простых сигналов
    """

    def __init__(self, frequency, sampling_frequency, seconds_duration, amplitude):
        """
        Конструктор
        :param frequency: частота (период)
        :param sampling_frequency: частота дискретизации
        :param seconds_duration: длительность в секундах
        :param amplitude: амплитуда
        """
        self.frequency = frequency
        self.sample_duration = sampling_frequency
        self.amplitude = amplitude
        self.duration = np.arange(0, seconds_duration + 1, 1 / sampling_frequency)
        self.signal = [0]

    def create_harmonic_signal(self):
        """
        Создает гармонический сигнал
        :return: гармонический сигнал
        """
        self.signal = np.zeros(len(self.duration))
        for i in range(len(self.duration)):
            self.signal[i] = self.amplitude * np.cos(self.frequency * self.duration[i])

    def create_triangular_signal(self):
        """
        Создает треугольный сигнал
        :return: треугольный сигнал
        """
        for i in range(len(self.duration)):
            self.signal[i] = self.amplitude * math.asin(np.sin(self.duration[i]))

    def create_pwm_signal(self):
        """
        Создает ШИМ сигнал
        :return: ШИМ сигнал
        """
        self.signal = np.zeros(len(self.duration))
        for i in range(len(self.duration)):
            sum = 0
            sum += np.sin((2 * i + 1) * self.frequency * self.duration[i])
            self.signal[i] = (4 * self.amplitude / np.pi) * sum

    def create_saw_signal(self):
        """
        Создает сигнал пилы
        :return: сигнал пилы
        """
        self.signal = np.zeros(len(self.duration))
        for i in range(len(self.duration)):
            sum = 0
            sum += ((-1) ** (i + 1)) * (1 / (i + 1)) * np.sin(i * self.frequency * self.duration[i])
            self.signal[i] = (2 * self.amplitude / np.pi) * sum

    def get_signal(self):
        """
        Возвращает сигнал целиком
        :return: сигнал (всю длительность в виде массива)
        """
        if self.signal[len(self.signal) - 1] != 0:
            plt.plot(self.duration, self.signal)
            plt.show()

        return self.signal

    def get_selection(self, sample_number):
        """
        Возвращает выборку сигнала
        :param sample_number: номер сэмпла
        :return: возвращает отдельную выборку сигнала номеру сэмпла или по отметке времени
        """
        seconds_duration = np.arange(0, sample_number, 1 / self.sample_duration)

        if self.signal[len(self.signal) - 1] != 0:
            signal = self.signal[:len(seconds_duration)]
            plt.plot(seconds_duration, signal)
            plt.show()
            print('Part of signal: Done!')
            return signal

    def next_selection(self, selection_length):
        """
        Функция-генератор следующую выборку
        :param selection_length: длина выборки
        :return: следующая выборка сигнала
        """
        length_selection = np.arange(selection_length, selection_length * 2, 1)
        for i in range(length_selection):
            signal = self.signal[i]
        plt.plot(length_selection, signal)
        plt.show()
        yield signal
