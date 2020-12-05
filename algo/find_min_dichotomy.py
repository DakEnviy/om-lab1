def find_min_dichotomy(func, left, right, epsilon):
    while (right - left) > epsilon:

        middle = (left + right) / 2
        x1 = middle - epsilon / 2.5
        x2 = middle + epsilon / 2.5
        val1 = func(x1)
        val2 = func(x2)

        if val1 == val2:
            left = x1
            right = x2

        if val1 < val2:
            right = x2

        if val2 < val1:
            left = x1

    return (left + right) / 2
