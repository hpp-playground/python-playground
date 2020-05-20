import numpy as np

n = 5

a = np.empty(shape=(n, 0))
print(a.shape)

test = np.array([1,1,1,1,1]).reshape([n, 1])
print(test)
print(test.shape)

a = np.append(a, test, axis=1)
print(a)
print(a.shape)