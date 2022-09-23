import matplotlib.pyplot as plt
from gen_simple_signal import Generator_simple
from gen_simple_nas import Generator_nas
from analyzer_signal import Analyzer
from chain_signal import Chain

samplee = 100
dd = 10
NN = samplee * dd


g00 = Generator_simple(NN, 3, 0.4, samplee, 1)
g11 = Generator_simple(NN, 1, 4, samplee, 1)
g22 = Generator_nas(g11, NN, 0, 0.4, samplee)
g33 = Generator_simple(NN, 2, 4, samplee, 1)
g44 = Generator_simple(NN, 0, 4, samplee, 1)
g55 = Generator_nas(g33, NN, 0, 0.4, samplee)
g66 = Generator_nas(g00, NN, 0, 0.4, samplee)

axx = plt.axes()
a00 = Analyzer(g00) 
a11 = Analyzer(g11)
a33 = Analyzer(g33)
a44 = Analyzer(g44)

a00.plot(axx)
a11.plot(axx)
a33.plot(axx)
a44.plot(axx)
plt.show()

axx = plt.axes()
a22 = Analyzer(g22)

a22.plot(axx)
a11.plot(axx)
plt.show()

axx = plt.axes()
a55 = Analyzer(g55)

a55.plot(axx)
a33.plot(axx)
plt.show()

axx = plt.axes()
cc = Chain(g22, False)

s_in, s_out = cc.get()

a22.plot(axx)
axx.plot(range(len(s_out)), s_out)
plt.show()

axx = plt.axes()
a66 = Analyzer(g66)

a66.plot_fft(axx)
plt.show()

axx = plt.axes()

a22.plot_rfft(axx)
plt.show()