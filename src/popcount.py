import time
import sys
from typing import Callable

def popcount_while(x: int) -> int:
    ret = 0
    while x:
        ret += x & 1
        x >>= 1
    return ret

def popcount_str(x: int) -> int:
    return bin(x).count("1")

def bit_count(x: int):
    x = (x & 0x5555555555555555) + ((x >> 1) & 0x5555555555555555)
    x = (x & 0x3333333333333333) + ((x >> 2) & 0x3333333333333333)
    x = (x + (x >> 4)) & 0x0f0f0f0f0f0f0f0f
    x += (x >>  8)
    x += (x >> 16)
    x += (x >> 32)
    return x & 0x7F

def measure(f: Callable[[int], int], iteration: int = 10**5):
    start = time.time()
    for i in range(iteration):
        _ = f(i)
    print(f"{f.__name__}:\t", time.time() - start)

def measure_longint(f: Callable[[int], int], value: int = (1 << 100000) - 1):
    start = time.time()
    _ = f(value)
    print(f"{f.__name__}:\t", time.time() - start)


if __name__ == "__main__":
    for f in [popcount_while, popcount_str, bit_count]:
        measure_longint(f)
