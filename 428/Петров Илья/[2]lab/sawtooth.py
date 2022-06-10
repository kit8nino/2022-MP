import numpy as np
import cmath as mt
from typing import Dict

class Sawtooth:
    def __init__(self , sizeIn : int = -1 , sizeOut : int = -1):
        self.isConvolve = False
        self.buff_in =  []
        self.size_buff_in = sizeIn
        self.buff_out = []
        self.size_buff_out = sizeOut

    def OnConvolve(self , frequenc_sec : float , amplitude : float):
        self.funConvolve = lambda t : (mt.cos(t/frequenc_sec)*amplitude).real
        self.isConvolve = True

    def OffConvolve(self):
        self.isConvolve = False

    def write(self , new_Values : Dict[float , float]):
        self.buff_in.clear()
        self.buff_in = new_Values.copy()
        if self.size_buff_in != -1:
            while len(self.buff_in) > self.size_buff_in:
                self.buff_in.pop(0)

        tmp_value = self.buff_in.copy()
        if self.isConvolve:
            signalConvolve = [self.funConvolve(t) for t in tmp_value]
            tmp_value_list : np.ndarray = np.convolve([x for x in tmp_value.values()] , signalConvolve)
            for it in zip(tmp_value_list , tmp_value):
                tmp_value[it[1]] = it[0]

        self.buff_out.clear()
        self.buff_out = tmp_value
        if self.size_buff_out != -1:
            while len(self.buff_out) > self.size_buff_out:
                self.buff_out.pop(0)

    def read(self):
        if len(self.buff_out) != 0:
            return self.buff_out.pop(-1)
        else:
            return None

    def readAll(self):
        return self.buff_out

    def read_yeld(self):
        for val in self.buff_out:
            yield val