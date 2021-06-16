# libreria pandas - exportar a excel

import pandas as pd

datos = {
    'first_name': ['Sigrid','Joe','Theodoric','Kennedy','Beatrix','Olimpis','Grange','Sallee'],
    'last_name':['Mannock','Hinners','Rivers','Donnell','Parlett','Guenther','Douce','Johnstone'],
    'age': [27,31,53,48,36,53,40,34],
    'amount_1': [7.17,1.90,1.11,1.41,6.69,4.62,1.01,4.88],
    'amount_2': [8.06,"?",5.90,"?","?",7.48,4.37,"?"]
}

df = pd.DataFrame(datos, columns=['first_name','last_name','age','amount_1','amount_2'])

ruta = r'c:\Users\israelarbonaguerrero\Desktop\MISION TIC 2022\CICLO_UNO\GRUPO_69\Semana 5\archivo3.xlsx'
df.to_excel(ruta, sheet_name='personas')