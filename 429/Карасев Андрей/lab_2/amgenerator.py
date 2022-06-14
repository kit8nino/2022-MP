from generator import Generator
import numpy as np


class AMGenerator(Generator):

    def __init__(self, frequency, sampling_frequency, seconds_duration, amplitude):

       Generator.__init__(self, frequency, sampling_frequency, seconds_duration, amplitude)

    def create_envelope_signal_modulation(self, amplitude, frequency):

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