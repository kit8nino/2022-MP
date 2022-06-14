import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

class butterfort():

    def __init__(self, signal, time):
        
        self.signal = signal
        self.time = time
        self.signal_temp = []

    def signal_transmission_without_changes(self):


        signal_end = self.signal 
        return signal_end

    def butter_filter(self):
        
        butter = []

        sos = signal.butter (4, 0.4, 'hp', fs = 1000, output = 'sos')
        butter=signal.sosfilt(sos, self.signal)
        if butter[len(butter) - 1] != 0:
            plt.plot(self.time,butter)
            plt.show()
        return butter

    def clipboard_storage(self, entered_time = 0):

        if entered_time == 0:
            self.signal_temp = self.signal

        if entered_time != 0:
            self.signal_temp = np.zeros(entered_time)
            self.signal_temp = self.signal[:entered_time]


    def return_full_signal(self):

        plt.plot(self.time, self.signal)
        plt.show()
        return self.signal

    def return_yield(self):
        plt.plot(self.time, self.signal)
        plt.show()

        yield self.signal 