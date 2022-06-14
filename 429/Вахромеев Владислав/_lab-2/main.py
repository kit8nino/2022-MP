from SimpleSignalGenerator import SimpleSignalGenerator
from AmplitudeModulatedSignal import AmplitudeModulatedSignal
from Curcuits import Curcuits
from Analyzer import Analyzer

main
modulated_signal = AmplitudeModulatedSignal(10, 1000, 20, 10)


modulated_signal.create_garmonic_signal()

signal = modulated_signal.return_the_signal()

modulated_signal.next_selection(99)

modulated_signal.create_modulated_signal(4, 1)

modulated_signal.return_the_signal()

analyzer = Analyzer(signal, modulated_signal.time)

analyzer.create_spectrum()

curcuits = Curcuits(signal, modulated_signal.time)

signal_f = curcuits.butter_filter()

analyzer_f = Analyzer(signal_f, modulated_signal.time)

analyzer_f.create_spectrum()