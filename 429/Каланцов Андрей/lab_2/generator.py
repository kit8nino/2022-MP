from math import sin, pi

class Generator:
    ''' Класс генератора простых сигналов '''
    def _f0(i, freq, period, amp):
        '''Функция для сигнала гармонической формы'''
        t = i / freq
        w = 2 * pi / period
        return amp * sin(w * t)

    def _f1(i, freq, period, amp):
        '''Функция для сигнала треугольной формы'''
        t = (i / freq) % period

        if t < period * 0.5:
            return 2*amp/period*t
        else:
            return -2*amp/period*t + 2*amp

    def _f2(i, freq, period, amp, skv=0.5):
        '''Функция для сигнала ШИМ формы со скважностью 0.5'''
        t = (i / freq) % period

        if t < period * skv:
            return amp
        else:
            return 0

    def _f3(i, freq, period, amp):
        '''Функция для сигнала пилообразной формы'''
        t = (i / freq) % period

        return amp/period*t


    _functions = [_f0, _f1, _f2, _f3]

    def __init__(self, total=1000, form=0, period=1, freq=100, amp=1, skv=0.5):
        self.period = period
        self.freq = freq
        self.amp = amp
        self.total = total
        self.duration = total / self.freq
        self.func = self._functions[form]


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
            yield self.get_by_index(i)