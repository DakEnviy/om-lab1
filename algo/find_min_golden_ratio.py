from math import sqrt


def find_min_golden_ratio(a, b, func, epsilon):
    x1 = a + ((3 - sqrt(5)) / 2) * (b - a)
    x2 = b - ((3 - sqrt(5)) / 2) * (b - a)
    val1 = func(x1)
    val2 = func(x2)
    while (b - a) > epsilon:

        if val1 == val2:
            a = x1
            b = x2
            x1 = a + ((3 - sqrt(5)) / 2) * (b - a)
            x2 = b - ((3 - sqrt(5)) / 2) * (b - a)
            val1 = func(x1)
            val2 = func(x2)

        if val2 < val1:
            a = x1
            x1 = x2
            x2 = b - ((3 - sqrt(5)) / 2) * (b - a)
            val1 = val2
            val2 = func(x2)
        if val1 < val2:
            b = x2
            x2 = x1
            x1 = a + ((3 - sqrt(5)) / 2) * (b - a)
            val2 = val1
            val1 = func(x1)

    return (a + b) / 2
