#!/usr/bin/env python
# coding: utf-8

# In[5]:


import generator_simple as sgen
import generator_complex as gen
from analyzer import Analyzer
from circut import Circut

def main():
    gen_simpl = sgen.generator_Simple()
    gen_simpl.setParametrs(2., 0.001, 5., 1.)
    signal1 = gen_simpl.getFullSignal()

    PWM_gen = sgen.generator_Simple()
    PWM_gen.setParametrs(0.1, 0.001, 5., 2.)
    signal2 = PWM_gen.getFullSignal()

    analiz_signal2 = Analyzer(signal2)
    analiz_signal2.show()

    modGen = gen.Generator_complex (  [signal1 ,signal2 ] , 0.001 , 20, 0.01, 5., 1 )
    signal3 = modGen.getFullSigna()
    analyz = Analyzer(signal3)
    # analyz.add_Fourier_spectrum()
    analyz.add_Dispersion()
    analyz.add_midl_Value()
    analyz.add_median_Value()
    analyz.add_min_Value()
    analyz.add_max_Value()
    analyz.show()
    circut  = Circut()
    circut.OnConvolve(0.1 , 0.1)
    circut.write(signal3)
    signal4 = chain.readAll()
    analyz = Analizer(signal4)
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


# In[ ]:




