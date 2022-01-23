import random

for _ in range(10):
    a = list(range(10))
    random.shuffle(a[2:8])
    print(a)

print(a[1:-1])