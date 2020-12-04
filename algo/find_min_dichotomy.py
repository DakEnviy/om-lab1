def find_min_dichotomy(a, b, func, epsilon):
    while (b - a) > epsilon:
        middle = (a + b) / 2
        x1 = middle - epsilon / 2
        x2 = middle + epsilon / 2
        val1 = func(x1)
        val2 = func(x2)
        if val1 == val2:
            a = x1
            b = x2
        if val1 < val2:
            a = x1
        if val2 < val1:
            b = x2

    return (a + b) / 2
