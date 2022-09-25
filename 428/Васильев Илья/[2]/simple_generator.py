import cmath as mt
import numpy as np

class Simple_generator:


    def __init__(self, typeSignal: str = "Harmonic" , parametr : float = 1.):
        self.amplitude = None
        self.duration = None
        self.period = None
        self.sampling_frequency = None
        self.t : float = 0.
        if typeSignal == "Harmonic":
            self.function_signal = lambda x: mt.sin(x * mt.pi)
        elif typeSignal == "Triangular":
            self.function_signal = lambda x: float(x) if float(x) < 0.5 else\
                float(1 - x) if float(x < 1.5) else float(x - 2.)
        elif typeSignal == "PWM":
            self.function_signal = lambda x: 1 if abs(x-1) < parametr/2 else 0
        elif typeSignal == "Saw":
            self.function_signal = lambda x: x/2
        else:
            self.function_signal = lambda x: 0

    def setParametrs(self, period_sec: float, sampling_frequency_sec: float,
                     duration_sec: float, amplitude: float):
        self.period = period_sec
        self.sampling_frequency = sampling_frequency_sec
        self.duration = duration_sec
        self.amplitude = amplitude

    def setPeriod_sec(self, period: float):
        self.period = period

    def setSampling_frequence_sec(self, sampling_frequency: float):
        self.sampling_frequency = sampling_frequency

    def setDuration_sec(self, duration: float):
        self.duration = duration

    def setDuration_sampl(self , duration : int):
        self.duration = duration * self.sampling_frequency

    def setAmplitude(self, amplitude: float):
        self.amplitude = amplitude

    def getFullSignal(self):
        res = dict()
        t : float = 0.
        while t <= self.duration:
            res = { **res , **self.getSignalForTime(t)}
            t += self.sampling_frequency
        return res

    def getSignalForSampl(self , t : int  ):
        return self.getSignalForTime(t*self.sampling_frequency)

    def getSignalForTime(self , t : float):
        return {t : self.function_signal((t/self.period) % 2)*self.amplitude}

    def getSignal(self):
        self.t = 0
        while self.t < self.duration:
            res = self.getSignalForTime(self.t)
            self.t += self.sampling_frequency
            yield res