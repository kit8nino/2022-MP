#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import matplotlib.pyplot as plt
from generator import Generator
from generator_mod import ModulatedGenerator
from analizer import Analizer
from circuit import Circuit

SAMPLE_RATE = 100
DURATION = 10
N = SAMPLE_RATE * DURATION

''' пилообразный сигнал '''
b0 = Generator(N, 3, 0.4, SAMPLE_RATE, 1) 
''' треугольный сигнал '''
b1 = Generator(N, 1, 4, SAMPLE_RATE, 1)
''' ШИМ сигнал '''
b3 = Generator(N, 2, 4, SAMPLE_RATE, 1)
''' гармонической сигнал '''
b4 = Generator(N, 0, 4, SAMPLE_RATE, 1)
''' огибающая для треугольного сигнала '''
b2 = ModulatedGenerator(b1, N, 0, 0.4, SAMPLE_RATE)
''' огибающая для ШИМ '''
b5 = ModulatedGenerator(b3, N, 0, 0.4, SAMPLE_RATE)
''' огибающая для пилообразного сигнала '''
b6 = ModulatedGenerator(b0, N, 0, 0.4, SAMPLE_RATE)

ax = plt.axes()
a0 = Analizer(b0)
a1 = Analizer(b1)
a3 = Analizer(b3)
a4 = Analizer(b4)

a0.plot(ax)
a1.plot(ax)
a3.plot(ax)
a4.plot(ax)
plt.show()
''' Огибающая для сигнала треугольной формы '''
ax = plt.axes()
a2 = Analizer(b2)

a2.plot(ax)
a1.plot(ax)
plt.show()

''' Огибающая для сигнала ШИМ формы '''
ax = plt.axes()
a5 = Analizer(b5)

a5.plot(ax)
a3.plot(ax)
plt.show()

''' треугольный сигнал, пройденный через фильтр'''
ax = plt.axes()
c = Circuit(b2, False)

s_in, s_out = c.get()

a2.plot(ax)
ax.plot(range(len(s_out)), s_out)
plt.show()
''' спектр фурье для пилообразного'''
ax = plt.axes()
a6 = Analizer(b6)

a6.plot_fft(ax)
plt.show()
''' Обратное преобразование Фурье треуг сигнала '''
ax = plt.axes()

a2.plot_rfft(ax)
plt.show()


