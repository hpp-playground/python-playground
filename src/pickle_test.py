import pickle


def hoge():
    a = [1, 2, 3, 4, 5]
    b = [6, 7, 8, 9, 10]

    with open("hoge.pickle", "wb") as f:
        pickle.dump(a, f)
        pickle.dump(b, f)


def fuga():
    with open("hoge.pickle", "rb") as f:
        a = pickle.load(f)
        b = pickle.load(f)
        print(a)
        print(b)


hoge()
fuga()
