from generator import Generator
from scipy import signal
from scipy.fft import rfft, rfftfreq, irfft
import numpy as np

class Circuit:

    def __init__(self, signal: Generator, filter_n=4, bypass=True):
        self.signal = signal
        self.filter_n = filter_n
        self.bypass = bypass
        self.input = []
        self.output = []

    def filter(self):
        yf = rfft(self.input)
        xf = rfftfreq(self.signal.total, 1/self.signal.freq)

        n = len(xf)

        ''' Прохождение сигнала через фильтр '''
        b, a = signal.b(self.filter_n, 0.4, 'low', analog=True)
        w, h = signal.freqs(b, a, xf)
        yf = [yf[i] * h[i] for i in range(n)]
        yf = irfft(yf)
        return yf

    def get(self):
        if not self.input:
            self.input = self.signal.get()

        if not self.output:
            if self.bypass:
                self.output = self.input.copy()
            else:
                self.output = self.filter()

        return self.input, self.output

    def __iter__(self):
        return self._gen()

    def _gen(self):
        s_input, s_output = self.get()
        i = 0
        n = len(s_input)
        for i in range(n):
            yield s_input[i], s_output[i]