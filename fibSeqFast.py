#! usr/bin/env python3

import time

def fib(x):
    x += 1  # so input produces expected value (i.e. 6 -> 8, 7 -> 13)
    f = [int(i) for i in range(0, x)]
    f[0] = 0
    f[1] = 1
    for j in range(2, x):
        f[j] = f[j - 1] + f[j - 2]
    return f[x - 1]


def time_test(x):
    start = time.time()
    print(fib(x), "time taken:", time.time() - start, sep="\n")

time_test(int(input()))
