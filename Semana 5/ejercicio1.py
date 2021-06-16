# libreria pandas - exportar a csv

import pandas as pd

datos = {
    'first_name': ['Sigrid','Joe','Theodoric'],
    'last_name':['Mannock','Hinners','Rivers'],
    'age': [27,31,53],
    'amount_1': [7.17,1.90,1.11],
    'amount_2': [8.06,"?",5.90]
}

datosDataFrame = pd.DataFrame(datos)

print(datosDataFrame)

ruta = r'c:\Users\israelarbonaguerrero\Desktop\MISION TIC 2022\CICLO_UNO\GRUPO_69\Semana 5\archivo1.csv'
datosDataFrame.to_csv(ruta, sep=',')