from SignalGenerator import SignalGenerator
from AMSignal import AMSignal
from Circuit import Circuit
from Analyzer import Analyzer

print('Номер моего Варианта: ', len("ТумбаевДанилаАлексеевич")%5)

garmonic_signal=AMSignal(5,1000,20,2,'График гармонического сигнала')
garmonic_signal.create_garmonic_signal()
signal=garmonic_signal.return_the_signal()


triangl_signal=AMSignal(5,1000,20,2,'График треугольного сигнала')
triangl_signal.create_triangl_signal()
signal1=triangl_signal.return_the_signal()
Circuit1 = Circuit(signal1, garmonic_signal.time)
signal_through_butter = Circuit1.butter_filter()

SHIM_signal=SignalGenerator(1,1,50,2,'График сигнала ШИМ')
SHIM_signal.create_SHIM_signal()
SHIM_signal.return_the_signal()

saw_signal=SignalGenerator(0.5,10,20,2,'График пилообразного сигнала')
saw_signal.create_saw_signal()
saw_signal.return_the_signal()


garmonic_signal.next_selection(99)
garmonic_signal.create_modulated_signal(4, 2.5)
garmonic_signal.return_the_signal()

Characters = Analyzer(signal, garmonic_signal.time)
Characters.characteristics()
Characters.create_spectrum()


Circuit = Circuit(signal, garmonic_signal.time)
Circuit.without_changes()
signal_through_butter = Circuit.butter_filter()

Characteristic_buffer = Analyzer(signal_through_butter, garmonic_signal.time)
Characteristic_buffer.characteristics()
Characteristic_buffer.create_spectrum()
