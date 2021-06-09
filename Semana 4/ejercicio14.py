# Libreria numpy - metodos creacion de matrices
# numerical python -> numpy

import numpy as np

matriz = np.zeros((3,3))
print(matriz)

matriz = np.ones((5,6))
print(matriz)

matriz = np.full((4,8), 'a')
print(matriz)

# matriz[0,0] = 2
# print(matriz)

matriz = np.eye(6)
print(matriz)

matriz = np.random.random((3,3))
print(matriz)