from Generator import Generator
from AM_Signal import AM_Signal
from Analyzer import Analyzer
from Сircuit import Circuit


frequency = 0.1
freq_dis = 8
time = 400
amplitude = 2
time_signal = 200

Signal_Generator = Generator(frequency, freq_dis, time, amplitude)


yn0 = [*Signal_Generator.Make_harm(time_signal)]


Signal_Analyzer0 = Analyzer(yn0, time_signal, freq_dis)
Signal_Analyzer0.Graph(1)
Signal_Analyzer0.Spectr()


Signal_Am = AM_Signal(frequency, yn0, time_signal, freq_dis, amplitude)
yn0 = Signal_Am.envelope()

Signal_Analyzer1 = Analyzer(yn0, time_signal, freq_dis)
Signal_Analyzer1.Graph(2)
Signal_Analyzer1.Dispersion(1)
Signal_Analyzer1.Average_Value(1)
Signal_Analyzer1.Median_Value(1)
Signal_Analyzer1.Max(1)
Signal_Analyzer1.Min(1)
Signal_Analyzer1.Scope(1)
Signal_Analyzer1.Spectr()


Cir = Circuit(yn0, time_signal, freq_dis)
Signal_Analyzer1.Graph(3)
Signal_Analyzer1.Spectr()

yn1 = Signal_Generator.Make_saw(time_signal)

Signal_Analyzer3 = Analyzer(yn1, time_signal, freq_dis)
Signal_Analyzer3.Graph(4)
Signal_Analyzer3.Spectr()


Signal_Am_1 = AM_Signal(frequency, yn1, time_signal, freq_dis, amplitude)
yn1 = Signal_Am_1.envelope()

Signal_Analyzer4 = Analyzer(yn1, time_signal, freq_dis)
Signal_Analyzer4.Graph(5)
Signal_Analyzer4.Dispersion(1)
Signal_Analyzer4.Average_Value(1)
Signal_Analyzer4.Median_Value(1)
Signal_Analyzer4.Max(1)
Signal_Analyzer4.Min(1)
Signal_Analyzer4.Scope(1)
Signal_Analyzer4.Spectr()


yn2 = Signal_Generator.Make_triangle(time_signal)
Signal_Analyzer2 = Analyzer(yn2, time_signal, freq_dis)
Signal_Analyzer2.Graph(6)
Signal_Analyzer2.Spectr()


#print(Signal_Am_1.get_signal_t(10), " Get AM signal t")
#print(Signal_Am_1.get_signal_n(10), " Get AM signal n")
#print([*(Signal_Generator.generator(30))], "Generator A signal")
#print([*(Signal_Am_1.generator(30))], "Generator AM signal")

