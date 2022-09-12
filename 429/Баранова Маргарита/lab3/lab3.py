import numpy as np

print()
print("Variant:", len("Баранова Маргарита Алексеевна")%5)
print()
print("2sin(x)-arctg(x)=0")

a=2.5
b=2.6

# 2sin(x)-arctg(x)=0
# x=tg(2sin(x))

def f_changed(x):
    return np.tan(2*np.sin(x))

def raznost(x):    
    return np.abs(f_changed(x)-f_changed(f_changed(x))) 

def reshenie_s_nuzhnoi_tochnostiyu(x):
    global a, b, e
    if raznost(x)<e and f_changed(x)>a and f_changed(x)<b:
        return f_changed(x)
    else:
        return reshenie_s_nuzhnoi_tochnostiyu(f_changed(x))

e=float(input("Vvedite nuzhuyu tochnost: "))

print("Naiden koren na promezhutke ot", a, "do", b)
print("Otvet: x=", reshenie_s_nuzhnoi_tochnostiyu(1))