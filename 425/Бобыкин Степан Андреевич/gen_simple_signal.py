# Класс генератора простых сигналов

from math import sin, pi


class Generator_simple():
    print('Generator --> signal')
    
    def garm(i, freq, period, amp): # гармонический сигнал
        t = i / freq
        w = 2 * pi / period
        return amp * sin(w * t)

    def trian(i, freq, period, amp): # треугольник
      
        t = (i / freq) % period
        if t < period * 0.5:
            return 2*amp/period*t
        else:
            return -2*amp/period*t + 2*amp

    def shim(i, freq, period, amp, skv=0.5): # ШИМ-сигнал (скважность 0.5)
        
        t = (i / freq) % period
        if t < period * skv:
            return amp
        else:
            return 0

    def saw(i, freq, period, amp): # пила
        t = (i / freq) % period
        return amp/period*t


    functions = [garm, trian, shim, saw]

    def __init__(self, total=1000, form=0, period=1, freq=100, amp=1, skv=0.5):
        self.period = period
        self.freq = freq
        self.amp = amp
        self.total = total
        self.duration = total / self.freq
        self.func = self.functions[form]


    def get(self):
        return [self.func(i, self.freq, self.period, self.amp) for i in range(self.total)]

    def get_by_index(self, i):
        return self.func(i, self.freq, self.period, self.amp)

    def get_by_time(self, t):
        i = round(t * self.freq)
        return self.func(i, self.freq, self.period, self.amp)

    def __iter__(self):
        return self._gen()

    def _gen(self):
        i = 0
        for i in range(self.total):
            yield self.get_by_index(i) # выборка