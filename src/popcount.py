import time
from typing import Callable


def make_bincountlist(x: int) -> None:
    res = [0]
    for _ in range(x.bit_length()):
        res += [j + 1 for j in res]


def popcount_while(x: int) -> int:
    ret = 0
    while x:
        ret += x & 1
        x //= 2
    return ret


def popcount_str(x: int) -> int:
    return bin(x).count("1")


def bit_count(x: int):
    x = (x & 0x5555555555555555) + ((x >> 1) & 0x5555555555555555)
    x = (x & 0x3333333333333333) + ((x >> 2) & 0x3333333333333333)
    x = (x + (x >> 4)) & 0x0F0F0F0F0F0F0F0F
    x += x >> 8
    x += x >> 16
    x += x >> 32
    return x & 0x7F


def measure(f: Callable[[int], int], iteration: int = 10**5):
    start = time.time()
    for i in range(iteration):
        _ = f(i)
    print(f"{f.__name__}:\t", time.time() - start)


if __name__ == "__main__":
    start = time.time()
    make_bincountlist(10**5)
    print(f"{make_bincountlist.__name__}:\t", time.time() - start)

    for f in [popcount_while, popcount_str, bit_count]:
        measure(f)
