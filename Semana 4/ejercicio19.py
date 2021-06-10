# Libreria numpy - indexación de matrices boolean

import numpy as np

'''
a = np.array([
    [1,2], 
    [3,4], 
    [5,6]
])

bool_idx = a > 2

print(bool_idx)

print(a[bool_idx])
print(a[a>4])
'''

# tipo de datos en matrices

x = np.array([1,2])
print(x.dtype)

x = np.array([1.0,2.0])
print(x.dtype)

x = np.array([1,2], dtype = np.float64)
print(x.dtype)