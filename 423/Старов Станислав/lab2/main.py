from SimpleSignalGenerator import SimpleSignalGenerator
from AmplitudeModulatedSignal import AmplitudeModulatedSignal
from Chains import Chains
from Analyzer import Analyzer
print("Вариант номер ", len("Старов Станислав Геннадьевич")%5)
modulated_signal = AmplitudeModulatedSignal(10, 10000, 40, 5)
modulated_signal.create_garmonic_signal()
signal = modulated_signal.return_the_signal()
modulated_signal.next_selection(99)
modulated_signal.create_modulated_signal(4, 1)
modulated_signal.return_the_signal()
analz = Analyzer(signal, modulated_signal.time)
analz.create_spectrum()
chains = Chains(signal, modulated_signal.time)
signal_f = chains.butter_filter()
 
