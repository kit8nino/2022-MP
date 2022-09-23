from scipy.fft import rfft, rfftfreq, irfft
from scipy import signal
from gen_simple_signal import Generator_simple

class Chain():
    print('signl_chain')
        
    def __init__(self, signall: Generator_simple, filter_nn=4, bypasss=True):
        self.signal = signall
        self.filter_n = filter_nn
        self.bypass = bypasss
        self.inputt = []
        self.outputt = []

    def bes(self):
        yff = rfft(self.inputt)
        xff = rfftfreq(self.signal.total, 1/self.signal.freq)
        nn = len(xff)
        bb, aa = signal.bessel(self.filter_n, 0.4, 'low', analog=True)
        ww, hh = signal.freqs(bb, aa, xff)
        yff = [yff[i] * hh[i] for i in range(nn)]
        yff = irfft(yff)
        return yff

    def get(self): 
        if not self.inputt:
            self.inputt = self.signal.get()

        if not self.outputt:
            if self.bypass:
                self.outputt = self.inputt.copy()
            else:
                self.outputt = self.bes()

        return self.inputt, self.outputt

    def __iter__(self):
        return self._gen()

    def _gen(self):
        s_inputt, s_outputt = self.get()
        i = 0
        n = len(s_inputt) 
        for i in range(n):
            yield s_inputt[i], s_outputt[i] # выборка 