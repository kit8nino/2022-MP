# mail file

a = len("БобыкинСтепанАндреевич")%5
print('Мой вариант:', a) # вариант 2 

import matplotlib.pyplot as plt
from gen_simple_signal import Generator_simple
from gen_simple_nas import Generator_nas
from analyzer_signal import Analyzer
from chain_signal import Chain

sample = 100
d = 10 # длительность
N = sample * d


g0 = Generator_simple(N, 3, 0.4, sample, 1) # пила
g1 = Generator_simple(N, 1, 4, sample, 1) # треугольник
g2 = Generator_nas(g1, N, 0, 0.4, sample) # Огибающая для сигнала треугольной формы
g3 = Generator_simple(N, 2, 4, sample, 1) # ШИМ - сигнал
g4 = Generator_simple(N, 0, 4, sample, 1) # гармонический сигнал
g5 = Generator_nas(g3, N, 0, 0.4, sample) # Огибающая для сигнала ШИМ формы
g6 = Generator_nas(g0, N, 0, 0.4, sample) # Огибающая для сигнала пилообразной формы

# Все созданные сигналы 
ax = plt.axes()
a0 = Analyzer(g0) 
a1 = Analyzer(g1)
a3 = Analyzer(g3)
a4 = Analyzer(g4)

a0.plot(ax)
a1.plot(ax)
a3.plot(ax)
a4.plot(ax)
plt.show()

ax = plt.axes()
a2 = Analyzer(g2) # Огибающая для сигнала треугольной формы

a2.plot(ax)
a1.plot(ax)
plt.show()

ax = plt.axes()
a5 = Analyzer(g5) # Огибающая для сигнала ШИМ формы

a5.plot(ax)
a3.plot(ax)
plt.show()

# ---------------------------------------------------

ax = plt.axes()
c = Chain(g2, False)

s_in, s_out = c.get()

a2.plot(ax)
ax.plot(range(len(s_out)), s_out) # Прохождение сигнала треугольной формы через фильтр Бесселя
plt.show()

ax = plt.axes()
a6 = Analyzer(g6)

a6.plot_fft(ax) # Спектр Фурье для сигнала пилообразной формы
plt.show()

ax = plt.axes()

a2.plot_rfft(ax) # Обратное преобразование Фурье для сигнала треугольной формы
plt.show()