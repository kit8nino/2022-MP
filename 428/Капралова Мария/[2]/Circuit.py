class Circuit():
    
    def __init__(self, yn, time, freq_dis):
        self.a = 1
        self.yn = yn
        self.t = time
        self.f_dis = freq_dis
        self.buffer = list()
        self.signal = list()
     
    def Get_Buffer(self, i): 
        if i < 0:
            return self.bufferх[0]
        return self.buffer[1]
    
    def No_Change(self):
        return self.yn
    
    def Return_Array(self):
        return self.buffer[1]
    
    def Return_Generator(self):
        for i in self.buffer[0]:
            yield i
