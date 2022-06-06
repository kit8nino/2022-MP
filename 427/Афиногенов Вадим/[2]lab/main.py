from signal_generator import signal_generator
from am_signal_generator import am_signal
from circuit import circuit
from analyzer import analyzer

print('(совместная работа Афиногенова Вадима и Антоновой Дарьи) вариант: ', len("Антонова Дарья Олеговна")%5)

garmonic_signal = am_signal(5, 1000, 20, 2, 'График гармонического сигнала')
garmonic_signal.create_garmonic_signal()
signal = garmonic_signal.return_the_signal()

triangl_signal = am_signal(5, 1000, 20, 2, 'График треугольного сигнала')
triangl_signal.create_triangl_signal()
signal1 = triangl_signal.return_the_signal()
сircuit1 = circuit(signal1, garmonic_signal.time)
signal_through_butter = сircuit1.butter_filter()

SHIM_signal = signal_generator(1, 1, 50, 2, 'График сигнала ШИМ')
SHIM_signal.create_SHIM_signal()
SHIM_signal.return_the_signal()

saw_signal = signal_generator(0.5, 10, 20, 2, 'График пилообразного сигнала')
saw_signal.create_saw_signal()
saw_signal.return_the_signal()

garmonic_signal.next_selection(99)
garmonic_signal.create_modulated_signal(4, 2.5)
garmonic_signal.return_the_signal()

сharacters = analyzer(signal, garmonic_signal.time)
сharacters.characteristics()
сharacters.create_spectrum()

circuit = circuit(signal, garmonic_signal.time)
circuit.without_changes()
signal_through_butter = circuit.butter_filter()

сharacteristic_buffer = analyzer(signal_through_butter, garmonic_signal.time)
сharacteristic_buffer.characteristics()
сharacteristic_buffer.create_spectrum()