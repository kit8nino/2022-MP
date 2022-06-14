from generator_simple import generator_simple
from generator_complex import generator_complex
from sawtooth import Sawtooth
from analyzer import analyzer


modulated_signal = generator_complex(10, 10000, 40, 5)

modulated_signal.create_garmonic_signal()

signal = modulated_signal.return_the_signal()

modulated_signal.next_selection(99)

modulated_signal.create_modulated_signal(4, 1)

modulated_signal.return_the_signal()

analyz = analyzer(signal, modulated_signal.time)
analyz.create_spectrum()


sawtooth = Sawtooth(signal, modulated_signal.time)

signal_f = sawtooth.butter_filter()

analyz_f = analyzer(signal_f, modulated_signal.time)
analyz_f.create_spectrum() 