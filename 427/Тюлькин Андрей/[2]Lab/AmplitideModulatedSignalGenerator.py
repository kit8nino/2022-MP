from SimpleSignalGenerator import SimpleSignalGenerator
import numpy as np


class AmplitudeModulatedSignalGenerator(SimpleSignalGenerator):
    """
        Класс-наследник генератора простых сигналов, содающий амлитудно-моделированный сигнал
    """

    def __init__(self, frequency, sampling_frequency, seconds_duration, amplitude):
        """
        Конструктор
        :param frequency: частота (период)
        :param sampling_frequency: частота дискретизации
        :param sample_duration: длительность в сэмплах
        :param seconds_duration: длительность в секундах
        :param amplitude: амплитуда
        """
        SimpleSignalGenerator.__init__(self, frequency, sampling_frequency, seconds_duration, amplitude)

    def create_envelope_signal_modulation(self, amplitude, frequency):
        """
        Создает огибающую в виде заранее заданного набора выборок (цифровой сигнал) с указанной частотой дискретизации
        этих выборок
        :param amplitude: амплитуда
        :param frequency: частота
        :return: огибающая
        """
        envelope = np.zeros(len(self.duration))
        for i in range(len(self.duration)):
            envelope[i] = amplitude * np.cos(frequency * self.duration[i])
        return envelope

    def create_amplitude_modulated_signal(self, amplitude, frequency):
        """
        Создает амплитудно-модулированный сигнал
        :param amplitude: амплитуда
        :param frequency: частота
        :return: огибающая
        """
        envelope = self.create_envelope_signal_modulation(amplitude, frequency)

        for i in range(len(self.duration)):
            self.signal[i] = amplitude * (1 + (self.amplitude / amplitude) * self.signal[i]) * envelope[i]
