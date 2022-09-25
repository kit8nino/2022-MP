# Класс-наследник генератора простых сигналов
from gen_simple_signal import Generator_simple

class Generator_nas(Generator_simple):
    print('Signal --> AM_signal')
    
    def __init__(self, amp_gen: Generator_simple, total=1000, form=0, period=1, freq=100):
        super().__init__(total, form, period, freq, 1)
        self.amp_gen = amp_gen
        self.amp_gen.total = total

    def get(self):
        amps = self.amp_gen.get()
        return [self.func(i, self.freq, self.period, amps[i]) for i in range(self.total)]

    def get_by_index(self, i):
        amp = self.amp_gen.get_by_index(i)
        return self.func(i, self.freq, self.period, amp)

    def get_by_time(self, t):
        i = round(t * self.freq)
        amp = self.amp_gen.get_by_index(i)
        return self.func(i, self.freq, self.period, amp) 