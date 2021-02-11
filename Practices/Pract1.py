import math


def cos(x):
    return math.cos(x)


def sin(x):
    return math.sin(x)


def ln(x):
    return math.log(x)


def tg(x):
    return math.tan(x)


def e(x):
    return math.exp(x)


def sqrt(x):
    return math.sqrt(x)


def func(x, y, z):
    return sin(x) - 66 * y ** 3 - 72 + z ** 6 + ((tg(55 * y ** 5 + 21 * z ** 8 + 6) - tg(z)) / (
            e(52 * z ** 2 - ((y ** 7) / 18) - 33) - (y ** 8) / 35)) - sqrt(e(z) - 76 * y ** 2)


# print (func(69, 72, 48))

def s_similar(x):
    if x < 128:
        return x ** 6 / 75 - 70 * x ** 7 + ln(x)
    elif (128 <= x) and (x < 183):
        return 50 * x ** 8 - x ** 4
    elif (183 <= x) and (x < 214):
        return 90 * x ** 3 + abs(x)
    elif x >= 214:
        return (x ** 3 - (x ** 2 / 75) - 60) ** 3 + x ** 5


# print(s_similar(86))
def partial_sums(n, m):
    res = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            res += (sin(j) - e(j))
    return res


def partial_sums1(n, m):
    res = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            res += (57 * i + e(j))
    return res


def iterration_summ(n, m):
    return partial_sums(n, m) + (partial_sums1(n, m)) / 52


# print(iterration_summ(16, 88))


def recurse(n):
    if n == 0: return 6
    if n == 1: return 3
    return cos(recurse(n - 2)) - sin(recurse(n - 2))


print(recurse(3))
