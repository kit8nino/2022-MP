import numpy as np

f = lambda x: np.log(1 + 2*x) - 2 + x

eps = lambda: float(input("Введите погрешность: "))

method = lambda a, b: a - f(a)*(a-b) / (f(a) - f(b))

break_method = lambda a, b , eps: np.fabs(f(a) - f(b)) < eps and np.fabs(b - a) < eps

solution = lambda a, b, eps: b if break_method(a, b, eps) else solution(method(a, b), method(a, b), eps)

minimum = lambda: 0.9
maximum = lambda: 1.

print("Chord method: x =", solution(minimum(), maximum(), eps()))
# Корень: x = 0.941304330652584