a = list(range(10))
for i, x in enumerate(a):
    print(i, x)
    del a[i]

print(a)