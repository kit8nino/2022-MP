#!/usr/bin/env python
# coding: utf-8

# In[2]:


{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7e34c586",
   "metadata": {},
   "outputs": [],
   "source": [
    "from Generator import Generator\n",
    "import numpy as np\n",
    "\n",
    "class Amplitude_modulated_signal(Generator):\n",
    "    \n",
    "    def __init__(self,freq,yn,duration,Sampling_freq,Aplitude):\n",
    "        self.xn=np.arange(0,duration,1./Sampling_freq)\n",
    "        self.freq=freq/20\n",
    "        self.Amplitude0=4\n",
    "        self.k=2\n",
    "        self.Freq0=20\n",
    "        self.yn=np.array(yn)\n",
    "        self.Sampling_freq=Sampling_freq\n",
    "        self.Aplitude=Amplitude\n",
    "        \n",
    "    \n",
    "    def get_freq(self,const):\n",
    "        self.freq=self.freq/const\n",
    "        \n",
    "        \n",
    "    def generator(self,duration):\n",
    "        xn=np.arange(self.xn[len(self.xn)-1],self.xn[len(self.xn)-1]+t,1./self.Sampling_freq)\n",
    "        for i in xn:\n",
    "            if self.xn[len(self.xn)-1]+t>=i:\n",
    "                yoeld(self.Amplitude0+self.k*self.save_yn)*np.cos(self.freq*i+self.Freq0*np.pi)\n",
    "        \n",
    "    def envelope(self):\n",
    "        self.save_yn=self.yn\n",
    "        self.yn=(self.Amplitude0+self.k*self.yn)*np.cos(self.freq*self.xn+self.Freq0*np.pi)\n",
    "        \n",
    "        return self.yn"
   ]
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


# In[ ]:




