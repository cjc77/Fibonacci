#! usr/bin/env python3

import time

def slow_fib(x):
    if x <= 1:
        return x
    else:
        return slow_fib(x - 1) + slow_fib(x - 2)

def time_test(x):
    start = time.time()
    print(slow_fib(x), "time taken:", time.time() - start, sep="\n")

time_test(int(input()))
