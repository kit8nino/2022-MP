from simple_signal_generator import simple_signal_generator
from AMS import AMS
from analyzer import Analyzer
from electrical_chain import Chain

print('Номер задания:', len("Биткин Сергей Юрьевич")%5)


modulated_signal = AMS(1, 10, 20, 1)

modulated_signal.generator_sin()

signal = modulated_signal.return_the_signal()


