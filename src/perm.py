import sys
from copy import deepcopy


def _perm(head: list, rest: list, result: list):
    if len(rest) == 0:
        # restを消費仕切ったら、結果に渡してあげる
        result.append(head)
        return
    for r in rest:
        # restからひとつ削ったrestxを生成
        restx = deepcopy(rest)
        restx.remove(r)

        # head に restから取り出した値を追加する
        headx = deepcopy(head)
        headx.append(r)

        _perm(headx, restx, result)


# サブっぽい関数に全部任せる
def perm(source: list) -> list:
    res = []
    _perm([], source, res)
    return res


def main():
    N = int(input())

    res = perm(list(range(1, N + 1)))
    print(res)


if __name__ == "__main__":
    main()
