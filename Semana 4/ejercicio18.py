# Libreria numpy - mutar matrices

import numpy as np

a = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [10,11,12]
])

print(a)
b = np.array([0,2,0,1])
print(b)
print(a[np.arange(4), b])
a[np.arange(4), b] += 10
print(a)