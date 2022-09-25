from math import sin, pi


class Generator_simple():
    print('Generatr --> signal')
    
    def garmm(i, freqq, periodd, ampp):
        t = i / freqq
        w = 2 * pi / periodd
        return ampp * sin(w * t)

    def triann(i, freqq, periodd, ampp):
      
        t = (i / freqq) % periodd
        if t < periodd * 0.5:
            return 2*ampp/periodd*t
        else:
            return -2*ampp/periodd*t + 2*ampp

    def shimm(i, freqq, periodd, ampp, skv=0.5):
        
        t = (i / freqq) % periodd
        if t < periodd * skv:
            return ampp
        else:
            return 0

    def saww(i, freqq, periodd, ampp):
        t = (i / freqq) % periodd
        return ampp/periodd*t


    functionss = [garmm, triann, shimm, saww]

    def __init__(self, totall=1000, formm=0, periodd=1, freqq=100, ampp=1, skv=0.5):
        self.periodd = periodd
        self.freqq = freqq
        self.ampp = ampp
        self.totall = totall
        self.duration = totall / self.freqq
        self.funcc = self.functionss[formm]


    def get(self):
        return [self.funcc(i, self.freqq, self.periodd, self.ampp) for i in range(self.totall)]

    def get_by_index(self, ii):
        return self.funcc(ii, self.freqq, self.periodd, self.ampp)

    def get_by_time(self, tt):
        ii = round(tt * self.freqq)
        return self.funcc(ii, self.freqq, self.periodd, self.ampp)

    def __iter__(self):
        return self._gen()

    def _gen(self):
        ii = 0
        for ii in range(self.totall):
            yield self.get_by_index(ii)