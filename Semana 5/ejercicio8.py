# archivo json

import json

datos = dict()
datos['clientes'] = []

datos['clientes'].append(
    {
        'pr_nombre': 'Juna',
        'sg_nombre': 'Clara',
        'edad': 27,
        'salario':7.17
    }
)

datos['clientes'].append(
    {
        'pr_nombre': 'Roberto',
        'sg_nombre': 'Luis',
        'edad': 31,
        'salario':[1.90,5.50]
    }
)

datos['clientes'].append(
    {
        'pr_nombre': 'Teodoro',
        'sg_nombre': 'Jaimes',
        'edad': 36,
        'salario':1.11
    }
)

ruta = r'c:\Users\israelarbonaguerrero\Desktop\MISION TIC 2022\CICLO_UNO\GRUPO_69\Semana 5\archivo8.json'

with open(ruta,'w')as file:
    json.dump(datos,file,indent=4)