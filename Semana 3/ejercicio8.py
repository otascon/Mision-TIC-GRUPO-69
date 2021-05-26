diccionarioEstudiantes = {
    'E3454fdf':{
        'nombres': 'Laura',
        'apellidos': 'Jaramillo',
        'acudientes': [
            {
                'acudiente_uno': 'Andrea',
                'acudiente_dos': 'Juan'
            },
            {
                'acudiente_uno': 'Fran',
                'acudiente_dos': 'Luis'
            }
        ],
        'promedio': 5.0
    },
    'Egg56dfg': {
        'nombres': 'Samir',
        'apellidos': 'Gómez',
        'acudientes': [
            {
                'acudiente_uno': 'Alejandro',
                'acudiente_dos': 'Sofía'
            }
        ],
        'promedio': 3.0
    },
    'FHT43523': {
        'nombres': 'Sara',
        'apellidos': 'Cabrera',
        'acudientes': [
            {
                'acudiente_uno': 'Carlos',
                'acudiente_dos': 'Amparo'
            }
        ],
        'promedio': 5.0
    },
    'Z4edkdf': {
        'nombres': 'Iván',
        'apellidos': 'Arcila',
        'acudientes': [
            {
                'acudiente_uno': 'Esposa',
                'acudiente_dos': ''
            },
            {
                'acudiente_uno': 'Mirian',
                'acudiente_dos': 'Pedro'
            },
            {
                'acudiente_uno': 'Ricardo',
                'acudiente_dos': 'Juliana'
            }
        ],
        'promedio': 4.0
    }
}


# print(diccionarioEstudiantes.keys())
# print(diccionarioEstudiantes.values())
# print(diccionarioEstudiantes.items())

'''
for elemento in diccionarioEstudiantes:
    print(elemento)
'''

'''
for x in diccionarioEstudiantes.items():
    for k in range(len(x)):
        print(x[k])
'''

'''
for codigoEstudiante, infoEstudiante in diccionarioEstudiantes.items():
    print('Llave : ', codigoEstudiante)
    print('Valor : ', infoEstudiante)
'''

'''
for codigoEstudiante, infoEstudiante in diccionarioEstudiantes.items():
    print(infoEstudiante['acudientes'])
'''

# Imprimir los acudientes_dos de todos los estudiantes

'''
for codigoEstudiante, infoEstudiante in diccionarioEstudiantes.items():
    print(infoEstudiante['acudientes'][0]['acudiente_dos'])
'''

'''
for codigoEstudiante, infoEstudiante in diccionarioEstudiantes.items():
    for x in infoEstudiante['acudientes']:
        print(x['acudiente_dos'])

        # print(infoEstudiante['acudientes'][x]['acudiente_dos'])
'''

'''
codigo =''
listaEstudiantes = list()
# Imprimir los estudiantes con promedio mayor a 4 y eliminar los demas estudiantes del dict
for codigoEstudiante, infoEstudiante in diccionarioEstudiantes.items():
    promedio = infoEstudiante['promedio']
    if promedio > 4:
        print('Estudiante : ' + infoEstudiante['nombres'] + ' '+ infoEstudiante['apellidos'])
    else:
       # diccionarioEstudiantes.pop(codigoEstudiante) 
       # codigo = codigoEstudiante
       listaEstudiantes.append(codigoEstudiante)
'''

'''
for reco in listaEstudiantes:
    # print(reco)
    diccionarioEstudiantes.pop(reco)
'''

'''
for reco_n in range(len(listaEstudiantes)):
    diccionarioEstudiantes.pop(listaEstudiantes[reco_n])
'''

'''
for reco_n in range(len(listaEstudiantes)):
    del diccionarioEstudiantes[listaEstudiantes[reco_n]]
'''

nuevosEstudiantes = diccionarioEstudiantes.copy()

for codigoEstudiante, infoEstudiante in nuevosEstudiantes.items():
    promedio = infoEstudiante['promedio']
    if promedio > 4:
        print('Estudiante : ', infoEstudiante['nombres'], ' ',infoEstudiante['apellidos'])
    else:
        diccionarioEstudiantes.pop(codigoEstudiante)

print(diccionarioEstudiantes)