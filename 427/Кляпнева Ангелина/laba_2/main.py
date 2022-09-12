from signal_gen import signal_gen
from modul_signal import modul_signal
from analyz import analyz
from butterfort import butterfort

f = 10
f_dis = 1000
t = 40
a = 5
t_sample = 150

A = modul_signal(f, f_dis, t, a)

A.create_garmonic_signal()

signal = A.return_the_signal()

A.next_selection(99)

A.create_modulated_signal(4, 1)

A.return_the_signal()

an = analyz(signal, A.time)
an.create_spectrum()


Butterfort = butterfort(signal, A.time)

signal_f = butterfort.butter_filter()

an_f = analyz(signal_f, A.time)
an_f.create_spectrum() 
