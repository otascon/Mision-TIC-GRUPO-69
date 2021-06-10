# Libreria pandas

from numpy import dtype
import pandas as pd

ventas = pd.Series([15,12,12],index = ["Ene", "Feb", "Mar"])

# print(ventas["Ene"])
# print(dtype(ventas))
# print(ventas.index)
# print(ventas.values)

ventas.name = "Ventas 2021"
ventas.index.name = "Meses"

print(ventas)

print(ventas.axes)
print(ventas.shape)