
from Generator import SimpleSignalGenerator
from Amplitud_signal import AmplitudeModulatedSignal
from Circut import Curcuits
from Analyzer import Analyzer

print("Номер задания:", len("Столяров Игорь Ильич")%5)
F = int(input("введите частоту гармонического сигнала"))
A = int(input("введите амплитуду гармонического сигнала"))
DF = int(input("введите частоту дискретизации гармонического сигнала"))
T = int(input("введите длительность гармонического сигнала"))
garm = AmplitudeModulatedSignal(F, DF, T, A)
garm.create_garmonic_signal()
signal1 = garm.return_the_signal()
garm.next_selection(99)
F = int(input("введите частоту 2ого сигнала"))
A = int(input("введите амплитуду 2ого сигнала"))
DF = int(input("введите частоту дискретизации 2ого сигнала"))
T = int(input("введите длительность 2ого сигнала"))
modulated_signal = AmplitudeModulatedSignal(F, DF, T, A)
print("Какого типа второй сигнал ?","1 - гармонический","2 - треугольный","3 - ШИМ","4 - пилообразный",sep = "/n")
n = int(input())
if (n is 1):
    modulated_signal.create_garmonic_signal()
elif (n is 2):
    modulated_signal.create_triangular_signal()
elif (n is 3):
    modulated_signal.create_pulse_width_modulation()
else:
    modulated_signal.create_signal_sawtooth()
s = input("Модулировать ли сигнал гармоникой?") 
if ((s is "Да") or (s is "Yes")):
    F = int(input("введите частоту модулирующего сигнала"))
    A = int(input("введите амплитуду модулирующего сигнала"))
    modulated_signal.create_modulated_signal(A, F)
signal2 = modulated_signal.return_the_signal()

analyzer = Analyzer(signal1, modulated_signal.time)

analyzer.create_spectrum()

curcuits = Curcuits(signal1, signal2, modulated_signal.time, modulated_signal.discrete_frequency)

signal_f = curcuits.convolution()

analyzer_f = Analyzer(signal_f, modulated_signal.time)

analyzer_f.create_spectrum()
