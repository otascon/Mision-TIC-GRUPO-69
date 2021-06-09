# Libreria numpy - indexación de matrices
# Rebanar

import numpy as np

a = np.array(
    [
        [1,2,3], 
        [5,6,7], 
        [9,10,11]
    ]
)

'''
# b = a[0:2,1:3]
[
    [2,3],
    [6,7]
]

# b = a[0:2,0:2]
[
    [1,2],
    [5,6]
]
'''


# print(a)
b = a[0:2,0:2]
# print(b)
# print(np.fliplr(a))


print(a[0, 1])
a[0, 1] = 77

print(a[0, 1])
