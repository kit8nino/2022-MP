import matplotlib.pyplot as plt
from generator import Generator
from generator_mod import ModulatedGenerator
from analizer import Analizer
from circuit import Circuit

SAMPLE_RATE = 100
DURATION = 10
N = SAMPLE_RATE * DURATION

''' Cигнал пилообразной формы '''
g0 = Generator(N, 3, 0.4, SAMPLE_RATE, 1) 
''' Cигнал треугольной формы '''
g1 = Generator(N, 1, 4, SAMPLE_RATE, 1)
''' Cигнал ШИМ формы '''
g3 = Generator(N, 2, 4, SAMPLE_RATE, 1)
''' Cигнал гармонической формы '''
g4 = Generator(N, 0, 4, SAMPLE_RATE, 1)
''' Огибающая для сигнала треугольной формы '''
g2 = ModulatedGenerator(g1, N, 0, 0.4, SAMPLE_RATE)
''' Огибающая для сигнала ШИМ формы '''
g5 = ModulatedGenerator(g3, N, 0, 0.4, SAMPLE_RATE)
''' Огибающая для сигнала пилообразной формы '''
g6 = ModulatedGenerator(g0, N, 0, 0.4, SAMPLE_RATE)

''' *************************************************************** '''
ax = plt.axes()
a0 = Analizer(g0)
a1 = Analizer(g1)
a3 = Analizer(g3)
a4 = Analizer(g4)

a0.plot(ax)
a1.plot(ax)
a3.plot(ax)
a4.plot(ax)
plt.show()
''' *************************************************************** '''
''' Огибающая для сигнала треугольной формы '''
ax = plt.axes()
a2 = Analizer(g2)

a2.plot(ax)
a1.plot(ax)
plt.show()
''' *************************************************************** '''
''' Огибающая для сигнала ШИМ формы '''
ax = plt.axes()
a5 = Analizer(g5)

a5.plot(ax)
a3.plot(ax)
plt.show()
''' *************************************************************** '''
''' Прохождение сигнала треугольной формы через фильтр'''
ax = plt.axes()
c = Circuit(g2, False)

s_in, s_out = c.get()

a2.plot(ax)
ax.plot(range(len(s_out)), s_out)
plt.show()
''' *************************************************************** '''
''' Спектр Фурье для сигнала пилообразной формы'''
ax = plt.axes()
a6 = Analizer(g6)

a6.plot_fft(ax)
plt.show()
''' *************************************************************** '''
''' Обратное преобразование Фурье для сигнала треугольной формы '''
ax = plt.axes()

a2.plot_rfft(ax)
plt.show()






