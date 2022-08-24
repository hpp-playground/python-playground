from dataclasses import dataclass


@dataclass
class Hoge:
    a: int


@dataclass
class Fuga(Hoge):
    b: int


if __name__ == "__main__":
    hoge = Hoge(1)
    fuga = Fuga(1, 2)
    fuga2 = Fuga(1, 2, c=3, d=4)
    print(hoge)
    print(fuga)
    print(fuga2)
