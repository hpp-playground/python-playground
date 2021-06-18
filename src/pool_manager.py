import os
from multiprocessing import Manager, Pool
from itertools import repeat


def hoge(i, d, s):
    d[i] = i
    s.add(i)

def main():
    with Manager() as manager, Pool(processes=os.cpu_count()) as pool:
        d = manager.dict()
        s = manager.set()
        pool.starmap(hoge, zip(range(100), repeat(d)), repeat(s))

        print(d)
        print(s)

if __name__ == "__main__":
    main()