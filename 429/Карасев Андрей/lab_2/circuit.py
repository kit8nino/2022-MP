import numpy as np
from scipy import signal
import matplotlib.pyplot as plt


class Circuit:

    def __init__(self, signal, duration):

        self.signal = signal
        self.duration = duration
        self.signal_temp = []

    def skip_signal_no_changes(self):

        return self.signal

    def filter_butter(self):

        butter = []

        sos = signal.butter(4, 0.4, 'hp', fs=1000, output='sos')
        butter = signal.sosfilt(sos, self.signal)
        if butter[len(butter) - 1] != 0:
            plt.plot(self.duration, butter)
            plt.show()

        return butter

    def storage(self, signal_duration):

        if signal_duration == 0:
            self.signal_temp = self.signal

        if signal_duration != 0:
            self.signal_temp = np.zeros(signal_duration)
            self.signal_temp = self.signal[:signal_duration]

    def get_signal(self):

        plt.plot(self.duration, self.signal)
        plt.show()

        return self.signal

    def yield_signal(self):

        plt.plot(self.duration, self.signal)
        plt.show()

        yield self.signal