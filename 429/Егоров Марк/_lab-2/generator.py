from builtins import super
import simple_generator
import numpy as np
from typing import *

class Generator(simple_generator.Simple_generator):

    def __init__(self, listSignals : List[Dict[float , float]] , frequence_signal_sec : float, \
                 period_sec: float, sampling_frequency_sec: float,
                 duration_sec: float, amplitude: float):
        super().__init__()
        super().setParametrs(period_sec, sampling_frequency_sec, duration_sec, amplitude)

        m_allSignals = dict()
        self.m_allTime = 0


        for selectSignals in listSignals:
            for t, value in selectSignals.items():
                if m_allSignals.get(t) is None:
                    m_allSignals[t] = 0
                m_allSignals[t] += value.real
                self.m_allTime = max(self.m_allTime, t)

        self.m_signal = dict()
        maxValue : float = max([abs(v) for v in m_allSignals.values()])


        for t in m_allSignals:
            self.m_signal[t] = (super().getSignalForTime(t)[t] * \
                               (1 + m_allSignals[t] / maxValue)).real

    def getFullSigna(self):
        return self.m_signal

    def getSignal(self):
        for t in self.m_signal:
            yield self.m_signal[t]