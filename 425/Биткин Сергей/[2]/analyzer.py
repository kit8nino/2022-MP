import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from scipy.fft import rfft, rfftfreq, irfft
from AMS import simple_signal_generator

class Analyzer():
    def __init__(self, signal:simple_signal_generator):
        self.signal = signal
        self.s = []
        pass

