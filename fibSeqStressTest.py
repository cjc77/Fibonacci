#! usr/bin/env python3
import random


def fast_fib(x):
    x += 1  # so input produces expected value (i.e. 6 -> 8, 7 -> 13)
    f = [int(i) for i in range(0, x)]
    if x <= 1:
        return x
    f[0] = 0
    f[1] = 1
    for j in range(2, x):
        f[j] = f[j - 1] + f[j - 2]
    return f[x - 1]


def slow_fib(x):
    if x <= 1:
        return x
    else:
        return slow_fib(x - 1) + slow_fib(x - 2)

while True:
    test = random.randrange(0, 12)
    x = fast_fib(test)
    y = slow_fib(test)
    print("Fast:", x)
    print("Slow:", y)
    if x != y:
        print("Error", x, y, sep="\n")
