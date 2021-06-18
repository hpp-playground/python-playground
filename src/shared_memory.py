from itertools import repeat
from multiprocessing import Value, Lock
from tqdm.contrib.concurrent import process_map


def hoge(args):
    i, lock, shared_set = args
    lock.aquire()
    shared_set.add(i)
    lock.release()

def main():
    lock = Lock()
    shared_set = Value(set, set())
    _ = process_map(hoge, zip(range(10), repeat(lock), repeat(shared_set)))
    print(shared_set)



if __name__ == "__main__":
    main()