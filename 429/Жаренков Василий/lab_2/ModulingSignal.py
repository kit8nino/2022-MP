from generatorSimpleS import GeneratorSimpleS
from AmplitudnoModulatedS import A_M_generator
from Chain import Chain
from Analization import Analization
print(len("ЖаренковВасилийАндреевич")%5)

modulated_signal = A_M_generator(10, 10000, 20, 10)

modulated_signal.create_garmonic_signal()

signal = modulated_signal.return_the_signal()

modulated_signal.next_selection(100)

modulated_signal.create_modulated_signal(1, 1)

modulated_signal.return_the_signal()

print(signal)

chain = Chain(signal, modulated_signal.time)

chain.bessel_filter()