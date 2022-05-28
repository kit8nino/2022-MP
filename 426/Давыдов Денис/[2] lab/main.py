from Generator import Generator
from AM_Signal import AM_Signal
from Analyzer import Analyzer
from Сircuit import Circuit

f = 0.1
f_dis = 8
t = 300
a = 1
t_sample = 150

A = Generator(f, f_dis, t, a)


yn = [*A.signal_harm_generator(t_sample)]


An = Analyzer(yn, t_sample, f_dis)
An.Graph(2)
An.Spectr()
An.Reverse_Fourier(1)

Am = AM_Signal(f, yn, t_sample, f_dis, a)
yn = Am.envelope()
An = Analyzer(yn, t_sample, f_dis)
An.Graph(3)
An.Dispersion(1)
An.Average_Value(1)
An.Median_Value(1)
An.Max(1)
An.Min(1)
An.Scope(1)
An.Spectr()
An.Reverse_Fourier(1)

Cir = Circuit(yn, t_sample, f_dis)
An = Analyzer(Cir.convolution(), t_sample, f_dis)
An.Graph(4)
An.Spectr()

ynn = A.CreateSignal_saw(t_sample)
An = Analyzer(ynn, t_sample, f_dis)
An.Graph(5)
An.Spectr()
An.Reverse_Fourier(1)

Am = AM_Signal(f, ynn, t_sample, f_dis, a)
ynn = Am.envelope()
An = Analyzer(ynn, t_sample, f_dis)
An.Graph(6)
An.Dispersion(1)
An.Average_Value(1)
An.Median_Value(1)
An.Max(1)
An.Min(1)
An.Scope(1)
An.Spectr()
An.Reverse_Fourier(1)

ynnn = A.CreateSignal_treug(t_sample)

An = Analyzer(ynnn, t_sample, f_dis)
An.Graph(7)
An.Spectr()

ynnnn = A.CreateSignal_SHIM(t_sample, 30)

An = Analyzer(ynnnn, t_sample, f_dis)
An.Graph(8)
An.Spectr()



print(Am.get_sample_t(10), " Am.get_sample_t")
print(Am.get_sample_n(10), " Am.get_sample_n")
print([*(A.generator(30))], "A.generator")
print([*(Am.generator(30))], "Am.generator")
print(*Cir.Return_Generator(), " = cir.return_generator")
