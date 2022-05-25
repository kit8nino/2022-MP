from AmplitideModulatedSignalGenerator import AmplitudeModulatedSignalGenerator
from SignalChain import SignalChain
from SignalAnalyzer import SignalAnalyzer

amplitude_modulated_signal_generator = AmplitudeModulatedSignalGenerator(10, 10000, 40, 5)

amplitude_modulated_signal_generator.create_harmonic_signal()
signal = amplitude_modulated_signal_generator.get_signal()

amplitude_modulated_signal_generator.next_selection(1000)
amplitude_modulated_signal_generator.create_amplitude_modulated_signal(4, 1)
amplitude_modulated_signal_generator.get_signal()

signal_analyzer = SignalAnalyzer(signal, amplitude_modulated_signal_generator.duration)
signal_analyzer.build_fourier_spectrum()

signal_chain = SignalChain(signal, amplitude_modulated_signal_generator.duration)
filtered_signal = signal_chain.filter_butter()

signal_analyzer_filtered = SignalAnalyzer(filtered_signal, amplitude_modulated_signal_generator.duration)
signal_analyzer_filtered.build_fourier_spectrum()
