# libreria pandas - leer csv

import pandas as pd

ruta = r'c:\Users\israelarbonaguerrero\Desktop\MISION TIC 2022\CICLO_UNO\GRUPO_69\Semana 5\archivo1.csv'

df = pd.read_csv(ruta, sep= ',', header=None)
# print(df)

df = pd.read_csv(ruta, skiprows=1,
names=['ID','First Name','Last Name','Age','Sales #1','Sales #2'])
# print(df)

df = pd.read_csv(ruta, skiprows=1,
names=['ID','First Name','Last Name','Age','Sales #1','Sales #2'],
na_values='?')
# print(df)

df = pd.read_csv(ruta, skiprows=1,
names=['ID','First Name','Last Name','Age','Sales #1','Sales #2'],
na_values='?',
index_col='ID')
print(df)

df = pd.read_csv(ruta, skiprows=1,
names=['ID','First Name','Last Name','Age','Sales #1','Sales #2'],
na_values='?',
index_col=['First Name', 'Last Name'])
print(df)























'''
cf = (13405.45 * 0.45)
consumo = (1100.80 * 0.45)
sub = (15 * consumo)

print(cf, consumo, sub)


vl_cf = (13405.45 - (13405.45 * 0.45))
val_sub_por_15_metros = (1100.80 - (1100.80 * 0.45))
vl_sub_15 = 15 * (1100.80 - (1100.80 * 0.45))
vl_sin_sub = ((72 - 15) * 1100.80)

print(vl_cf, val_sub_por_15_metros,vl_cf + vl_sub_15 + vl_sin_sub)
'''