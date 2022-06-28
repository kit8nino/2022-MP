# Основной код
from gen_simple.py import Gen_simple
from gen_heir.py import Gen_heir
from analyzer.py import Analyzer
from circuit.py import Circuit

f = 0.1
f_dis = 8
t = 300
a = 1
t_sample = 150

A = Gen_simple(f, f_dis, t, a)


yn = [*A.signal_harm_generator(t_sample)]

An = Analyzer(yn, t_sample, f_dis)
An.Graph(2)
An.Spectr()
An.Reverse_Fourier(1)

Cir = Circuit(yn, t_sample, f_dis)
An = Analyzer(Cir.convolution(), t_sample, f_dis)
An.Graph(4)
An.Spectr()

Am =  Gen_heir(f, yn, t_sample, f_dis, a)
yn = Am.envelope()
An = Analyzer(yn, t_sample, f_dis)
An.Graph(3)
An.Spectr()

print(Am.get_sample_t(10), " Am.get_sample_t")
print(Am.get_sample_n(10), " Am.get_sample_n")
print([*(A.generator(30))], "A.generator")
print([*(Am.generator(30))], "Am.generator")
print(*Cir.Return_Generator(), " = cir.return_generator")

