#!/usr/bin/env python
# coding: utf-8

# In[1]:


#сделали Миронов и Поздоровкин
from generator_simple import Generator_simple
from generator_complex import Generator_complex
from analyzer import Analyzer
from circut import Circut
print('Номер моего Варианта: ', len("Миронов  Андрей Алексеевич")%5)
f=0.1
f_0=5
t=500
Ampl=1
t_s=250
A=Generator_simple(f,f_0,t,Ampl)
y_n=[*A.Signal_Harmonic(t_s)]
An=Analyzer(y_n,t_s,f_0)
An.Graph(2)
An.Spectr()
An.Reverse_Fourier(1)
Am=Generator_complex(f,y_n,t,f_0,Ampl)
y_n=Am.envel()
An=Analyzer(y_n,t_s,f_0)
An.Graph(3)
An.Disper(1)
An.Average(1)
An.Median(1)
An.Max(1)
An.Min(1)
An.Scope(1)
An.Spectr()
An.Reverse_Fourier(1)
Cir=Circut(y_n,t_s,f_0)
An=Analyzer(Cir.convol(),t_s,f_0)
An.Graph(4)
An.Spectr()
y_nn=A.Signal_w(t_s)
An=Analyzer(y_nn,t_s,f_0)
An.Graph(5)
An.Spectr()
An.Reverse_Fourier(1)
Am=Generator_complex(f,y_nn,t_s,f_0,Ampl)
y_nn=Am.envelope()
An=Analyzer(y_nn,t_s,f_0)
An.Graph(6)
An.Disper(1)
An.Average(1)
An.Median(1)
An.Max(1)
An.Min(1)
An.Scope(1)
An.Spectr()
An.Reverse_Fourier(1)
y_nnn=A.Signal_triag(t_s)
An=Analyzer(y_nnn,t_s,f_0)
An.Graph(7)
An.Spectr()
y_nnnn=A.Signal_SHIM(t_s,30)
An=Analyzer(y_nnnn,t_s,f_0)
An.Graph(8)
An.Spectr()
print(Am.get_sample_t(10), " Am.get_sample_time")
print(Am.get_sample_n(10), " Am.get_sample_n")
print([*(A.generator(30))], "A.generator")
print([*(Am.generator(30))], "Am.generator")
print(*Cir.Return_Gener(), "=cir.return_gener")


# In[ ]:




