import math

K = (3 - math.sqrt(5)) / 2


def _sign(x):
    return math.copysign(1, x)


def find_min_brent(func, left, right, epsilon=0.0005):
    a, c = left, right
    x = w = v = a + K * (c - a)
    fx = fw = fv = func(x)
    d = e = c - a

    while abs(x - (a + c) / 2) + (c - a) / 2 >= 2 * epsilon:
        g = e
        e = d

        u = None

        # Параболлическая аппроксимация
        # x, w, v - разные и fx, fw, fv - разные
        if x != w and x != v and w != v and fx != fw and fx != fv and fw != fw:
            u_temp = x - \
                ((x - w) ** 2 * (fx - fv) - (x - v) ** 2 * (fx - fw)) / \
                2 / ((x - w) * (fx - fv) - (x - v) * (fx - fw))

            if a + epsilon <= u_temp <= c - epsilon and abs(u_temp - x) < g / 2:
                u = u_temp

        # Золотое сечение
        if u is None:
            if x < (a + c) / 2:
                u = x + K * (c - x)
                e = c - x
            else:
                u = x - K * (x - a)
                e = x - a

        if abs(u - x) < epsilon:
            u = x + _sign(u - x) * epsilon

        d = abs(u - x)
        fu = func(u)

        if fu <= fx:
            if u >= x:
                a = x
            else:
                c = x

            v, fv = w, fw
            w, fw = x, fx
            x, fx = u, fu
        else:
            if u >= x:
                c = u
            else:
                a = u

            if fu <= fw or w == x:
                v, fv = w, fw
                w, fw = u, fu
            elif fu <= fv or v == x or v == w:
                v, fv = u, fu

    return x
