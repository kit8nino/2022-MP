from Simplesig import Simplesig
from Amplitudemodulatedsignal  import Amplitudemodulatedsignal
from Tzepy import Tzepy
from Analyzator import Analyzator


modulated_signal = AmpModSig(10, 10000, 40, 5)

modulated_signal.create_garmonic_signal()

signal = modulated_signal.return_the_signal()

modulated_signal.next_selection(99)

modulated_signal.create_modulated_signal(4, 1)

modulated_signal.return_the_signal()

analz = Analyzator(signal, modulated_signal.time)
analz.create_spectrum()


chains = Tzepy(signal, modulated_signal.time)

signal_f = chains.butter_filter()

anal_f = Analyzator(signal_f, modulated_signal.time)
anal_f.create_spectrum() 
