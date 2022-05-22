from SimpleSignalGenerator import SimpleSignalGenerator
from AmplitudeModulatedSignal import AmplitudeModulatedSignal
from Chains import Chains
from Analyzer import Analyzer

print('Номер задания:', len("Неводчиков Иван Владимирович")%5)

modulated_signal = AmplitudeModulatedSignal(10, 10000, 40, 5)

modulated_signal.create_garmonic_signal()

signal = modulated_signal.return_the_signal()

modulated_signal.next_selection(99)

modulated_signal.create_modulated_signal(4, 1)

modulated_signal.return_the_signal()

print(signal)

chains = Chains(signal, modulated_signal.time)

chains.butter_filter()