from gen_simple_signal import Generator_simple

class Generator_nas(Generator_simple):
    print('Signl --> AM_signal')
    
    def __init__(self, amp_genn: Generator_simple, totall=1000, formm=0, periodd=1, freqq=100):
        super().__init__(totall, formm, periodd, freqq, 1)
        self.amp_genn = amp_genn
        self.amp_genn.total = totall

    def get(self):
        amps = self.amp_genn.get()
        return [self.func(ii, self.freq, self.period, amps[ii]) for ii in range(self.total)]

    def get_by_index(self, ii):
        amp = self.amp_genn.get_by_index(ii)
        return self.func(ii, self.freq, self.period, amp)

    def get_by_time(self, tt):
        ii = round(tt * self.freq)
        amp = self.amp_genn.get_by_index(ii)
        return self.func(ii, self.freq, self.period, amp) 

