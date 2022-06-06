from Generator import Generator
from AM_Signal import AM_Signal
from Analyzer import Analyzer
from Сircuit import Circuit

frequency = 0.1 
sampling_rate = 8
t = 300
a = 1
t_sample = 150

A = Generator(frequency, sampling_rate, t, a)


yn = [*A.signal_harm_generator(t_sample)]


An_s = Analyzer(yn, t_sample, sampling_rate)
An_s.Graph(2)
An_s.Spectr()
An_s.Reverse_Fourier(1)

Am = AM_Signal(frequency, yn, t_sample, sampling_rate, a)
yn = Am.envelope()
An_s = Analyzer(yn, t_sample, sampling_rate)
An_s.Graph(3)
An_s.Dispersion(1)
An_s.Average_Value(1)
An_s.Median_Value(1)
An_s.Max(1)
An_s.Min(1)
An_s.Scope(1)
An_s.Spectr()
An_s.Reverse_Fourier(1)

Cir = Circuit(yn, t_sample, sampling_rate)
An_s = Analyzer(Cir.convolution(), t_sample, sampling_rate)
An_s.Graph(4)
An_s.Spectr()

ynn = A.CreateSignal_saw(t_sample)
An_s = Analyzer(ynn, t_sample, sampling_rate)
An_s.Graph(5)
An_s.Spectr()
An_s.Reverse_Fourier(1)

Am = AM_Signal(frequency, ynn, t_sample, sampling_rate, a)
ynn = Am.envelope()
An_s = Analyzer(ynn, t_sample, sampling_rate)
An_s.Graph(6)
An_s.Dispersion(1)
An_s.Average_Value(1)
An_s.Median_Value(1)
An_s.Max(1)
An_s.Min(1)
An_s.Scope(1)
An_s.Spectr()
An_s.Reverse_Fourier(1)

ynnn = A.CreateSignal_treug(t_sample)

An_s = Analyzer(ynnn, t_sample, sampling_rate)
An_s.Graph(7)
An_s.Spectr()

ynnnn = A.CreateSignal_SHIM(t_sample, 30)

An_s = Analyzer(ynnnn, t_sample, sampling_rate)
An_s.Graph(8)
An_s.Spectr()



print(Am.get_sample_t(10), " Am.get_sample_t")
print(Am.get_sample_n(10), " Am.get_sample_n")
print([*(A.generator(30))], "A.generator")
print([*(Am.generator(30))], "Am.generator")
print(*Cir.Return_Generator(), " = cir.return_generator")