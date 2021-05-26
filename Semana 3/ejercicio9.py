diccionarioEstudiantes = {
    'E3454fdf':{
        'nombres': 'Laura',
        'apellidos': 'Jaramillo',
        'acudientes': [
            'Andrea',
            'Juan'
        ],
        'promedio': 5.0
    },
    'Egg56dfg': {
        'nombres': 'Samir',
        'apellidos': 'Gómez',
        'acudientes': [
            'Alejandro',
            'Sofía'
        ],
        'promedio': 3.0
    },
    'FHT43523': {
        'nombres': 'Sara',
        'apellidos': 'Cabrera',
        'acudientes': [
            'Carlos',
            'Amparo'
        ],
        'promedio': 5.0
    },
    'Z4edkdf': {
        'nombres': 'Iván',
        'apellidos': 'Arcila',
        'acudientes': [
            'Esposa'
        ],
        'promedio': 4.0
    }
}

for codigoEstudiante, infoEstudiante in diccionarioEstudiantes.items():
    for acudiente in infoEstudiante['acudientes']:
        print('Acudiente : ', acudiente)

# [('E3454fdf',{'nombres': 'Laura','apellidos': 'Jaramillo','acudientes': ['Andrea','Juan']})]