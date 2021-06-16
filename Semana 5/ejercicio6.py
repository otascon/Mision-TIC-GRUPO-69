# archivos txt
# import pandas as pd

datos = ['linea uno','linea dos','linea tres','linea 4','linea 5']

ruta = r'c:\Users\israelarbonaguerrero\Desktop\MISION TIC 2022\CICLO_UNO\GRUPO_69\Semana 5\archivo6.txt'
ruta_2 = r'c:\Users\israelarbonaguerrero\Desktop\MISION TIC 2022\CICLO_UNO\GRUPO_69\Semana 5\archivo6_2.txt'

fichero = open(ruta,'w')
for lin in datos:
    fichero.write(lin)
    fichero.write('\n')
fichero.close()

fichero2 = open(ruta_2,'w')
for lin in datos:
    print(lin, file=fichero2)
fichero2.close()







