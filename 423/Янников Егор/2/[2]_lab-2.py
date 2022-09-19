import numpy as np
import math as m
import matplotlib.pyplot as plt
from numpy.fft import fft
import scipy as sp

class SimpleSignalGenerator:

    def __init__(self, frequency, frequency_diskret, time_in_sec, amplitude):


        self.frequency = frequency
        self.frequency_diskret = frequency_diskret
        self.amplitude = amplitude
        self.time = np.arange(0, time_in_sec + 1, 1 / frequency_diskret)
        self.signal = [0]

    def create_garmonic_signal(self):


        self.signal = np.zeros(len(self.time))
        for i in range(len(self.time)):
            self.signal[i] = self.amplitude * np.cos(self.frequency * self.time[i])

        print('Create garmonic signal: Done!')

    def create_triangular_signal(self):



        self.signal = np.zeros(len(self.time))
        for i in range(len(self.time)):
            self.signal[i] = self.amplitude * m.asin(np.sin(self.time[i]))

        print('Done!')

    def create_pulse_width_modulation(self):


        self.signal = np.zeros(len(self.time))
        for i in range(len(self.time)):
            summ = 0
            summ += np.sin((2 * i + 1) * self.frequency * self.time[i])
            self.signal[i] = (4 * self.amplitude / np.pi) * summ

        print('Done!')    
        pass

    def create_signal_saw(self):



        self.signal = np.zeros(len(self.time))
        for i in range(len(self.time)):
            summ = 0
            summ += ((-1)**(i + 1)) * (1 / (i+1)) * np.sin(i * self.frequency * self.time[i])
            self.signal[i] = (2 * self.amplitude / np.pi) * summ

        print('Done!')    
        pass

    def return_the_signal(self):



        if self.signal[len(self.signal) - 1] != 0:
            plt.plot(self.time, self.signal)
            plt.show()

        print('Full signal: Done!')
        return self.signal

    def return_the_selection(self, entered_time):



        time = np.arange(0, entered_time, 1 / self.frequency_diskret)

        if self.signal[len(self.signal) - 1] != 0:
            signal = self.signal[:len(time)]
            plt.plot(time, signal)
            plt.show()
            print('Part of signal: Done!') 
            return signal

    def next_selection(self, lenght_selection):



        lenght_selection = np.arange(lenght_selection, lenght_selection * 2, 1)
        for i in range(lenght_selection):
            signal = self.signal[i]
        plt.plot(lenght_selection, signal)
        plt.show()

        print('Next selection: Done!') 
        yield signal

class Analyzer():

    def __init__(self, signal, time):



        self.signal = signal
        self.time = time
        self.max_signal = 0
        self.min_signal = 0
        self.razmah = 0
        self.spect = 0
        self.frq = 0

    def create_spectrum(self):

        n = len(self.signal) 
        k = np.arange(n)
        T = n
        frq = k/T 
        frq = frq[range(n//2)] 

        Y = fft(self.signal)/n 
        Y = Y[range(n//2)]
        plt.plot(frq,abs(Y),'r') 
        plt.show()
        self.spect = Y

        self.frq = frq


        print('Create Fourier spectrum: Done!')
        pass

    def сounting_characteristics(self):

        self.max_signal = max(self.signal)
        self.min_signal = min(self.signal)

        self.razmah = abs(self.max_signal) + abs(self.min_signal)


        print('Максимальное значение сигнала:', self.max_signal)
        print('Минимальное значение сигнала:', self.min_signal)
        print('Размах сигнала:', self.razmah)
        print('Counting characteristics: Done!')
        pass

    def inverse_fourier_transform(self):

        fig, axs = plt.subplots(1, 2)
        n_bins = len(self.signal)
        axs[0].hist(self.signal['sepal length (cm)'], bins=n_bins)
        axs[0].set_title('sepal length')
        axs[1].hist(self.signal['petal length (cm)'], bins=n_bins)
        axs[1].set_title('petal length')

        print('Inverse Fourier transform: Done!')
        pass 

class Chains():

    def __init__(self, signal, time):

        self.signal = signal
        self.time = time
        self.signal_temp = []

    def signal_transmission_without_changes(self):

        signal_end = self.signal # конечный вид сигнала, после прохождения цепи

        print('Signal transmission without changes: Done!')
        return signal_end

    def butter_filter(self):


        butter = []

        sos = signal.butter (4, 0.4, 'hp', fs = 1000, output = 'sos')
        butter=signal.sosfilt(sos, self.signal)
        if butter[len(butter) - 1] != 0:
            plt.plot(self.time,butter)
            plt.show()
        print(butter)
        print('Butter Filter: Done!')
        return butter

    def clipboard_storage(self, entered_time = 0):

        if entered_time == 0:
            self.signal_temp = self.signal

        if entered_time != 0:
            self.signal_temp = np.zeros(entered_time)
            self.signal_temp = self.signal[:entered_time]

        print('Clipboard storage: Done!')

    def return_full_signal(self):

        plt.plot(self.time, self.signal)
        plt.show()

        print('Return full signal: Done!')
        return self.signal

    def return_yield(self):

        plt.plot(self.time, self.signal)
        plt.show()

        print('Return yield: Done!')    
        yield self.signal 




class AmplitudeModulatedSignal(SimpleSignalGenerator):

    def __init__(self, frequency, frequency_discret, time_in_sec, amplitude):
        SimpleSignalGenerator.__init__(self, frequency, frequency_discret, time_in_sec, amplitude)

    def create_eveloping(self, amplitude, frequency):

             eveloping = np.zeros(len(self.time))
        for i in range(len(self.time)):    
            eveloping[i] = amplitude * np.cos(frequency * self.time[i])
        return eveloping

    def create_modulated_signal(self, amplitude, frequency): 

        eveloping = self.create_eveloping(amplitude, frequency)

        for i in range(len(self.time)):
            self.signal[i] = amplitude * (1 + (self.amplitude / amplitude) * self.signal[i]) * eveloping[i] 

        print('Create modulated signal: Done!')         


print("Вариант 3")

modulated_signal = AmplitudeModulatedSignal(10, 10000, 40, 5)

modulated_signal.create_garmonic_signal()

signal = modulated_signal.return_the_signal()

modulated_signal.next_selection(99)

modulated_signal.create_modulated_signal(4, 1)

modulated_signal.return_the_signal()

analz = Analyzer(signal, modulated_signal.time)
analz.create_spectrum()


chains = Chains(signal, modulated_signal.time)

signal_f = chains.butter_filter()

anal_f = Analyzer(signal_f, modulated_signal.time)
anal_f.create_spectrum() 
