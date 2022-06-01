from generator_simple import Generator_simple
from generator_complex import Generator_complex
from analyzer import Analyzer
from circuit import Circuit

#print(len("Хохряков Даниил Алексеевич")%5)

the_signal = Generator_complex(10, 10000, 30, 10)
the_signal.garmonic_signal()

signal = the_signal.full_signal()
the_signal.generator_func(100)
the_signal.am_signal(1, 1)
the_signal.full_signal()

print(signal)

circuits = Circuit(signal, the_signal.time)
circuits.sawtooth_convolution()