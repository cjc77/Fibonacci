#! usr/bin/env python3

import time

def fib(x):
    if n < 2:
        return n
    else:
        n1, n2 = 1, 1
        for i in range(2, n):
            new_n = n1 + n2
            n2 = new_n
            n1 = n2
    return n2


def time_test(x):
    start = time.time()
    print(fib(x), "time taken:", time.time() - start, sep="\n")

time_test(int(input()))
