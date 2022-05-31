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

def reshenie_s_nuzhnoi_tochnostiyu(x):
    global otvet, e
    fx=f_changed(x)
    if np.abs(fx-f_changed(fx))<e and fx>a and fx<b:
        otvet=fx
        return
    else:
        reshenie_s_nuzhnoi_tochnostiyu(f_changed(x))
    return

e=float(input("Vvedite nuzhuyu tochnost: "))

reshenie_s_nuzhnoi_tochnostiyu(1)

print("Naiden koren na promezhutke ot", a, "do", b)
print("Otvet: x=", otvet)