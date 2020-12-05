import math


def func1(x):
    return -5 * x ** 5 + 4 * x ** 4 - 12 * x ** 3 + 11 * x ** 2 - 2 * x + 1


def func2(x):
    return math.log10(x - 2) ** 2 + math.log10(10 - x) ** 2 - x ** 0.2


def func3(x):
    return -3 * x * math.sin(0.75 * x) + math.exp(-2 * x)


def func4(x):
    return math.exp(3 * x) + 5 * math.exp(-2 * x)


def func5(x):
    return 0.2 * x * math.log10(x) + (x - 2.3) ** 2


epsilon = 1e-4
places = 4

test_functions = [
    (func1, -0.5, 0.5, 0.10986),
    (func2, 6, 9.9, 8.72691),
    (func3, 0, 2 * math.pi, 2.70648),
    (func4, 0, 1, 0.2408),
    (func5, 0.5, 2.5, 2.2219)
]

test_functions_multi = [
    (func3, -15, 0, -0.00009)  # actual minimum is -31.667
]
