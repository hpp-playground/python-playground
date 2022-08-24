import os
from concurrent.futures import ProcessPoolExecutor


def hoge(args):
    print(args)


def main():
    with ProcessPoolExecutor(
        max_workers=os.cpu_count(), initargs=("huga, hoge", "foo")
    ) as executor:
        res = executor.map(hoge, range(10))

    print(list(res))


if __name__ == "__main__":
    main()
