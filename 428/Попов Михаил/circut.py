{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "ea4fc2a1",
   "metadata": {},
   "outputs": [],
   "source": [
    "import scipy.signal\n",
    "import matplotlib.pyplot as plt\n",
    "from numpy.fft import rfft, rfftfreq, fft, ifft\n",
    "import numpy as np\n",
    "import math as m\n",
    "\n",
    "class Circut():\n",
    "    \n",
    "    def __init__(self,yn,duration,Sampling_freq):\n",
    "        self.Amplitude=1\n",
    "        self.yn=yn\n",
    "        self.duration=duration\n",
    "        self.Sampling_freq=Sampling_freq\n",
    "        self.buffer=list()\n",
    "        self.signal=list()\n",
    "    \n",
    "    def convolution(self):\n",
    "        xn = np.arange(0, self.duration, 1 / self.Sampling_freq)\n",
    "        harm=self.Amplitude * np.cos(self.xn[i] * self.freq)\n",
    "        self.buffer.append(self.yn)\n",
    "        self.buffer.append(self.yn*harm)\n",
    "        self.signal=self.yn*harm\n",
    "        \n",
    "        return (self.yn*saw)\n",
    "    \n",
    "    def get_buffer(self,i):\n",
    "        if i<0:\n",
    "            return self.buffer[0]\n",
    "        return self.buffer[1]\n",
    "    \n",
    "    def No_change(self):\n",
    "        return self.yn\n",
    "    \n",
    "    def Return_array(self):\n",
    "        return self.buffer[1]\n",
    "    \n",
    "    def Return_generator(self):\n",
    "        for i in self.buffer[0]:\n",
    "            yield i\n",
    "        \n",
    "        "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "17496f3f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e415096b",
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
