fib_buf = [1, 1]


def fib(n):
    if n < 0:
        raise ValueError()

    if n < len(fib_buf):
        return fib_buf[n]

    v = fib(n - 1) + fib(n - 2)
    fib_buf.append(v)
    return v


def find_min_fibonacci(a, b, func, epsilon):
    fn = (b - a) / epsilon

    n = 2
    while fib(n) < fn:
        n += 1

    x1 = a + fib(n - 2) / fib(n) * (b - a)
    x2 = a + fib(n - 1) / fib(n) * (b - a)
    val1 = func(x1)
    val2 = func(x2)

    while n > 2:
        n -= 1

        if val1 > val2:
            a = x1

            x1 = x2
            x2 = a + fib(n - 1) / fib(n) * (b - a)

            val1 = val2
            val2 = func(x2)
        else:
            b = x2

            x2 = x1
            x1 = a + fib(n - 2) / fib(n) * (b - a)

            val2 = val1
            val1 = func(x1)

    return (a + b) / 2
