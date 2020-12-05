
def find_min_parabola(func, a, b, epsilon=0.0005):
    x1, x2, x3 = a, (a + b) / 2, b
    f1, f2, f3 = func(x1), func(x2), func(x3)

    while abs(x3 - x1) >= epsilon:
        u = x2 -\
            ((x2 - x1) ** 2 * (f2 - f3) - (x2 - x3) ** 2 * (f2 - f1)) /\
            2 / ((x2 - x1) * (f2 - f3) - (x2 - x3) * (f2 - f1))
        fu = func(u)

        if fu <= f2:
            if u <= x2:
                x3, f3 = x2, f2
            else:
                x1, f1 = x2, f2
            x2, f2 = u, fu
        else:
            if u <= x2:
                x1, f1 = u, fu
            else:
                x3, f3 = u, fu

    return (x1 + x2) / 2
