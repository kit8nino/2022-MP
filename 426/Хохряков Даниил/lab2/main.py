from generator_simple.py import Generator_simple
from generator_complex.py import Generator_complex
from analyzer.py import Analyzer
from circuit.py import Circuit

print(len("Хохряков Даниил Алексеевич")%5)

modulated_signal = Generator_complex(10, 10000, 20, 10)

modulated_signal.create_garmonic_signal()

signal = modulated_signal.return_the_signal()

modulated_signal.next_selection(100)

modulated_signal.create_modulated_signal(1, 1)

modulated_signal.return_the_signal()

print(signal)

circuits = Circuit(signal, modulated_signal.time)

circuits.bessel_filter()