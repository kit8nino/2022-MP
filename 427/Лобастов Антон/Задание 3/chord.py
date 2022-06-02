#%%
import numpy as np

f = lambda x: np.log(1 + 2*x) - 2 + x

epsilon = lambda: float(input('Введите погрешность: '))

method = lambda a, b: a - f(a)*(a-b) / (f(a)-f(b))

stop = lambda a, b, e: np.fabs(f(a)-f(b)) < e

solution = lambda a, b, e : b if stop(a,b,e) else solution(method(b, a), method(a, b), e)


min = lambda: 0.9
max = lambda: 1


print('Chord  method:\nx =', solution(min(), max(), epsilon()))
# x = 0.941304330652584
# %%
