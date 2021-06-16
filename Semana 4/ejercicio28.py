# libreria pandas

import pandas as pd

entradas = pd.Series([11,18,12,16,9,16,22,28,31,29,30,12],
index=['ene','feb','mar','abr','may','jun','jul','ago','sep','oct','nov','dic'])
# print(entradas)

salidas = pd.Series([9,16,12,16,9,16,10,28,31,29,20,12],
index=['ene','feb','mar','abr','may','jun','jul','ago','sep','oct','nov','dic'])

almacen = pd.DataFrame({"entradas": entradas, "salidas": salidas})
almacen['neto'] = almacen.entradas - almacen.salidas

print(almacen)

print(entradas.head())
print(almacen.head())