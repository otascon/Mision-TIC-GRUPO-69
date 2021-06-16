# libreria pandas - dataFrames

import pandas as pd

datos = {'manzanas': [3,2,0,1], 'naranjas': [0,3,7,2]}

compras = pd.DataFrame(datos, index=['Juan','Roberto','Elias','David'])
# print(compras)

# print(compras.index)
# print(compras.columns)
# print(compras.axes)

compras.index.name = 'Clientes'
compras.columns.name = 'Frutas'

print(compras)

