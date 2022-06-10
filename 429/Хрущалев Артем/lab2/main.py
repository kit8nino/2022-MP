from amgenerator import AMGenerator
from circuit import Circuit
from analyzer import Analyzer

AMSignalGenerator = AMGenerator(10, 10000, 40, 5)

AMSignalGenerator.create_harmonic_signal()
signal = AMSignalGenerator.get_signal()

AMSignalGenerator.next_selection(1000)
AMSignalGenerator.create_amplitude_modulated_signal(4, 1)
AMSignalGenerator.get_signal()

signalAnalyzer = Analyzer(signal,AMSignalGenerator.duration)
signalAnalyzer.build_fourier_spectrum()

signalCircuit = Circuit(signal, AMSignalGenerator.duration)
filteredSignal = signalCircuit.filter_butter()

signalAnalyzerFiltered = Analyzer(filteredSignal, AMSignalGenerator.duration)
signalAnalyzerFiltered.build_fourier_spectrum()