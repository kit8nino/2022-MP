import Simple_generator as sgen
import Generator as gen
from Analyzat_signal import Analyzat_signal
from Chain import Chain

def main():
    simpl_gen = sgen.Simple_generator()
    simpl_gen.setParametrs(2., 0.001, 5., 1.)
    signal1 = simpl_gen.getFullSignal()

    PWM_gen = sgen.Simple_generator()
    PWM_gen.setParametrs(0.1, 0.001, 5., 2.)
    signal2 = PWM_gen.getFullSignal()

    analiz_signal2 = Analyzat_signal(signal2)
    analiz_signal2.show()

    modGen = gen.Generator(  [signal1 ,signal2 ] , 0.001 , 20, 0.01, 5., 1 )
    signal3 = modGen.getFullSigna()
    analyz = Analyzat_signal(signal3)
    # analyz.add_Fourier_spectrum()
    analyz.add_Dispersion()
    analyz.add_midl_Value()
    analyz.add_median_Value()
    analyz.add_min_Value()
    analyz.add_max_Value()
    analyz.show()
    chain  = Chain()
    chain.OnConvolve(0.1 , 0.1)
    chain.write(signal3)
    signal4 = chain.readAll()
    analyz = Analyzat_signal(signal4)
    #analyz.add_Fourier_spectrum()
    analyz.add_Dispersion()
    analyz.add_midl_Value()
    analyz.add_median_Value()
    analyz.add_min_Value()
    analyz.add_max_Value()
    analyz.show()



def get_gen():
    for i in range(10):
        yield i

if __name__ == '__main__':
    main()