a = [[]] * 5
a[0].append(1)
print(a)
print([id(ai) for ai in a])

b = [[] for _ in range(5)]
b[0].append(1)
print(b)
print([id(bi) for bi in b])

c = [None] * 5
for i in range(5):
    c[i] = []
print(c)
