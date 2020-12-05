from math import sqrt


def find_min_golden_ratio(func, left, right, epsilon):
    x1 = left + ((3 - sqrt(5)) / 2) * (right - left)
    x2 = right - ((3 - sqrt(5)) / 2) * (right - left)
    val1 = func(x1)
    val2 = func(x2)
    while (right - left) > epsilon:

        if val1 == val2:
            left = x1
            right = x2
            x1 = left + ((3 - sqrt(5)) / 2) * (right - left)
            x2 = right - ((3 - sqrt(5)) / 2) * (right - left)
            val1 = func(x1)
            val2 = func(x2)

        if val2 < val1:
            left = x1
            x1 = x2
            x2 = right - ((3 - sqrt(5)) / 2) * (right - left)
            val1 = val2
            val2 = func(x2)
        if val1 < val2:
            right = x2
            x2 = x1
            x1 = left + ((3 - sqrt(5)) / 2) * (right - left)
            val2 = val1
            val1 = func(x1)

    return (left + right) / 2
