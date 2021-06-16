# libreria pandas - excel

import pandas as pd

ruta = r'c:\Users\israelarbonaguerrero\Desktop\MISION TIC 2022\CICLO_UNO\GRUPO_69\Semana 5\archivo3.xlsx'

df = pd.read_excel(ruta, header= None, skiprows=1)
print(df)

df = pd.read_excel(ruta, skiprows=1,
            names=['Id','Pr Nombre','Sg Nombre','Edad','Salario 1','Salario 2'])
print(df)
