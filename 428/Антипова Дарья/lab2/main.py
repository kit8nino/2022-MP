#!/usr/bin/env python
# coding: utf-8

# In[ ]:


{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "502922b2",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'null' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-10-3e976eafabd1>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[1;31m#from Analyzer import Analyzer\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      4\u001b[0m \u001b[1;31m#from circut import Circut\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 5\u001b[1;33m \u001b[1;32mimport\u001b[0m \u001b[0mGenerator\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mpy\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      6\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mAmplitude_modulated_signal\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mpy\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      7\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mAnalyzer\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mpy\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;32m~\\Desktop\\prog\\Generator.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m     79\u001b[0m   {\n\u001b[0;32m     80\u001b[0m    \u001b[1;34m\"cell_type\"\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;34m\"code\"\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 81\u001b[1;33m    \u001b[1;34m\"execution_count\"\u001b[0m\u001b[1;33m:\u001b[0m \u001b[0mnull\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     82\u001b[0m    \u001b[1;34m\"id\"\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;34m\"c23da0db\"\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     83\u001b[0m    \u001b[1;34m\"metadata\"\u001b[0m\u001b[1;33m:\u001b[0m \u001b[1;33m{\u001b[0m\u001b[1;33m}\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'null' is not defined"
     ]
    }
   ],
   "source": [
    "#from Generator import Generator\n",
    "#from Amplitude_modulated_signal import Amplitude_modulated_signal\n",
    "#from Analyzer import Analyzer\n",
    "#from circut import Circut\n",
    "import Generator.py\n",
    "import Amplitude_modulated_signal.py\n",
    "import Analyzer.py\n",
    "import circut.py\n",
    "\n",
    "freq=0.2\n",
    "Sampling_freq=4\n",
    "duration=300\n",
    "Ampllitude=1\n",
    "t_sample=150\n",
    "\n",
    "\n",
    "A=Generator(freq,Sampling_freq,duration,Amplitude)\n",
    "\n",
    "yn=[*A.CreateSignal_Harmonic(t_sample)]\n",
    "\n",
    "An=Analyzer(yn,t_sample,Sampling_freq)\n",
    "An.Graph(2)\n",
    "An.Spectr()\n",
    "An.Reverse_Fourier(1)\n",
    "\n",
    "Am=Amplitude_modulated_signal(freq,yn,t_sample,Sampling_freq)\n",
    "yn=Am.envelope()\n",
    "An=Analyzer(yn,t_sample,Sampling_freq)\n",
    "An.Graph(3)\n",
    "An.Dispersion(1)\n",
    "An.Avarage_value(1)\n",
    "An.Median_value(1)\n",
    "An.Max(1)\n",
    "An.Min(1)\n",
    "An.Scope(1)\n",
    "An.Spectr()\n",
    "An.Reverse_Fourier(1)\n",
    "\n",
    "Cir=Circut(yn,t_sample,Sampling_freq)\n",
    "An=Analyzer(Cir.convolution(),t_sample,Sampling_freq)\n",
    "An.Graph(4)\n",
    "An.Spectr()\n",
    "\n",
    "ynn= A.CreateSignal_Saw(t_sample)\n",
    "An=Analyzer(ynn,t_sample,Sampling_freq)\n",
    "An.Graph(5)\n",
    "An.Spectr()\n",
    "An.Reverse_Fourier(1)\n",
    "\n",
    "Am=Amplitude_modulated_signal(freq,ynn,t_sample,Sampling_freq,Amplitude)\n",
    "ynn=Am.envelope()\n",
    "An=Analyzer(ynn,t_sample,Sampling_freq)\n",
    "An.Graph(6)\n",
    "An.Dispersion(1)\n",
    "An.Avarage_value(1)\n",
    "An.Median_value(1)\n",
    "An.Max(1)\n",
    "An.Min(1)\n",
    "An.Scope(1)\n",
    "An.Spectr()\n",
    "An.Reverse_Fourier(1)\n",
    "\n",
    "ynnn=A.CreateSignal_triangle(t_sample)\n",
    "\n",
    "An=Analyzer(ynnn,t_sample,Sampling_freq)\n",
    "An.Graph(7)\n",
    "An.Spectr()\n",
    "\n",
    "ynnnn=A.CreateSignal_SHIM(t_sample,30)\n",
    "\n",
    "An=Analyzer(ynnnn,t_sample,Sampling_freq)\n",
    "An.Graph(8)\n",
    "An.Spectr()\n",
    "\n",
    "print(Am.get_sample_duration(10),\"Am.get_sample_duration\")\n",
    "print(Am.get_sample_n(10),\"Am.get_sample_n\")\n",
    "print([*(A.Generator(30))], \"A.Generator\")\n",
    "print([*(Am.Generator(30))], \"Am.Generator\")\n",
    "print(*Cir.Return_Generator(), \" = cir.return_generator\")\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d41b2aa4",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

