import numpy as np

n = 5

a = np.empty(shape=(n, 1, 0))
print(a.shape)

test = np.array([1] * n * 5).reshape((n, 1, 5))

a = np.append(a, test, axis=2)

print(a)
print(a.shape)
