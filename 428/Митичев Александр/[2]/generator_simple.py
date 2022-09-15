import numpy as np
from scipy import signal

class Generator_simple():
    def __init__(self,fr,fr_0,time,Ampl):
            self.fr=fr
            self.fr_0=fr_0
            self.time=time
            self.Ampl=Ampl
            self.count=0
    def Signal_Harmonic(self,time):
        self.x_new=np.arange(0,time, 1./self.fr_0)
        for i in range(len(self.x_new)):
            yield (self.Ampl*np.cos(self.x_new[i]*self.fr))
    def Signal_SHIM(self,time,pr_cycles):
        if time<=0:
            time=self.time
        pr=pr_cycles
        dt=1/self.fr_0
        x_new=np.arange(0,time,dt); 
        self.y_new=self.Ampl*x_new%(1/self.fr)<(1/self.fr)*0.01*pr
        return self.y_new
    def Signal_triang(self,time):
        if time<=0:
            time=self.time
        x_new=np.arange(0,time,1./self.fr_0)
        self.y_new=self.Ampl*signal.sawtooth(2*np.pi*self.fr*x_new)
        return self.y_new
    def get_sample_n(self,n): 
        return self.y_new[n]
    def Signal_w(self,time):
        if time<=0:
            time=self.time
        x_new=np.arange(0,time,1./self.fr_0)
        y_new=np.exp((complex(-(1/2),self.fr))*x_new)
        self.y_new=np.angle(y_new)*self.Ampl/3
        return self.y_new
    def generator(self, time): 
        x_new=np.arange(self.x_new[len(self.x_new)-1],self.x_new[len(self.x_new)-1]+time,1./self.fr_0)
        for i in range(len(x_new)):   
            yield (self.Ampl*np.cos(x_new[i]*self.fr))
    def get_sample_time(self,time): 
        print(len(self.y_new))
        print(time*self.fr_0)
        return self.y_new[time*self.fr_0]  