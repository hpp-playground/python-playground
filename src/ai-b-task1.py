import math


def l2norm(v):
    return sum(vi*vi for vi in v)

def dot_product(v1, v2):
    assert len(v1) == len(v2)
    return sum(v1i*v2i for v1i, v2i in zip(v1, v2))

def cossim(v1, v2):
    assert len(v1) == len(v2)
    return dot_product(v1,v2) / math.sqrt(l2norm(v1) * l2norm(v2))

def main():
    hierogriphs = [
        [51, 20, 84, 0, 3, 0],
        [52, 58, 4, 4, 6, 26],
        [115, 83, 10, 42, 33, 17],
        [59, 39, 23, 4, 0, 0],
        [98, 14, 6, 2, 1, 0],
        [12, 17, 3, 2, 9, 27],
        [11, 2, 2, 0, 18, 0],
    ]
    query = hierogriphs[2]

    for hierogriph in hierogriphs:
        print(cossim(query, hierogriph))

    print("-"*40)

    word_counts = [sum(v) for v in hierogriphs]
    context_counts = [sum(c) for c in zip(*hierogriphs)]
    count_sum = sum(word_counts)

    eps = 1e-9
    pmi_matrix = [
        [
            max(0, math.log(vi+eps) + math.log(count_sum) - math.log(wc+eps) - math.log(cc+eps))
            for cc, vi in zip(context_counts, v)
        ]
        for wc, v in zip(word_counts, hierogriphs)
    ]

    query = pmi_matrix[2]
    for pmis in pmi_matrix:
        print(cossim(query, pmis))


if __name__ == "__main__":
    main()