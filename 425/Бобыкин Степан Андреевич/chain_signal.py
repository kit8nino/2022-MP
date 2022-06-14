# Класс цепи
from scipy.fft import rfft, rfftfreq, irfft
from scipy import signal
from gen_simple_signal import Generator_simple

class Chain():
    print('signal_chain')
        
    def __init__(self, signal: Generator_simple, filter_n=4, bypass=True):
        self.signal = signal
        self.filter_n = filter_n
        self.bypass = bypass
        self.input = []
        self.output = []

    def bes(self): # Прохождение сигнала через фильтр Бесселя 
        yf = rfft(self.input)
        xf = rfftfreq(self.signal.total, 1/self.signal.freq)
        n = len(xf)
        b, a = signal.bessel(self.filter_n, 0.4, 'low', analog=True)
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
                self.output = self.bes()

        return self.input, self.output

    def __iter__(self):
        return self._gen()

    def _gen(self):
        s_input, s_output = self.get()
        i = 0
        n = len(s_input) 
        for i in range(n):
            yield s_input[i], s_output[i] # выборка 