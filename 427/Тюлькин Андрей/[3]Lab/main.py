import numpy as np


def f(x):
    return np.log10(1 + 2 * x) - 2 + x


def chord_method(left, right, e):
    result = None
    if f(left) * f(right) < 0:
        while abs(left - right) > e:
            mid = left - f(left) * (right - left) / (f(right) - f(left))
            if f(mid) == 0 or abs(f(mid)) < e:
                result = mid
                break
            elif f(left) * f(mid) < 0:
                right = mid
            elif f(right) * f(mid) < 0:
                left = mid
    return result


if __name__ == '__main__':
    epsilon = float(input('Введите точность: '))
    left = float(input('Введите начало отрезка: '))
    right = float(input('Введите конец отрезка: '))
    root = chord_method(left, right, epsilon)
    print(f'Корень: {root}') if root else print('Корень не найден!')
