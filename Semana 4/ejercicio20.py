# Libreria numpy - matematicas de matriz

import numpy as np

x = np.array([[1,2],[3,4]], dtype=np.float64)
y = np.array([[5,6],[7,8]], dtype=np.float64)


# Sumar matrices
print(x + y)
print(np.add(x,y))

# Resta matrices
print(x - y)
print(np.subtract(x, y))


# Multiplicar matrices
print(x * y)
print(np.multiply(x,y))

# Dividir matrices
print(x / y)
print(np.divide(x, y))

# Raiz cuadrada de elementos
print(np.sqrt(x))


