fib_buf = [1, 1]


def fib(n):
    if n < 0:
        raise ValueError()

    if n < len(fib_buf):
        return fib_buf[n]

    v = fib(n - 1) + fib(n - 2)
    fib_buf.append(v)
    return v


def find_min_fibonacci(func, left, right, epsilon):
    fn = (right - left) / epsilon

    n = 2
    while fib(n) < fn:
        n += 1

    x1 = left + fib(n - 2) / fib(n) * (right - left)
    x2 = left + fib(n - 1) / fib(n) * (right - left)
    val1 = func(x1)
    val2 = func(x2)

    while n > 2:
        n -= 1

        if val1 > val2:
            left = x1

            x1 = x2
            x2 = left + fib(n - 1) / fib(n) * (right - left)

            val1 = val2
            val2 = func(x2)
        else:
            right = x2

            x2 = x1
            x1 = left + fib(n - 2) / fib(n) * (right - left)

            val2 = val1
            val1 = func(x1)

    return (left + right) / 2
