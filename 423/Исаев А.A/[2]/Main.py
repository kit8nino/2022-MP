from SimpleSignalGenerator import SimpleSignalGenerator
from AmplitudeModulatedSignal import AmplitudeModulatedSignal
from Chains import Chains
from Analyzer import Analyzer


modulated_signal = AmplitudeModulatedSignal(10, 10000, 20, 10)

modulated_signal.create_garmonic_signal()

signal = modulated_signal.return_the_signal()

modulated_signal.next_selection(100)

modulated_signal.create_modulated_signal(1, 1)

modulated_signal.return_the_signal()

print(signal)

chains = Chains(signal, modulated_signal.time)

chains.bessel_filter()