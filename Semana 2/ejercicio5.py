'''
{} llaves
[] corchetes
() parentesis
'''
'''
dicccionario = {
    "total": 55,
    "descuento": True, 
    15 : "15" 
}


print(dicccionario)
otro_dicccionario = {'nombre': 12-3,'telefono': 3205555555, 'edad': 28,'ciudad': 'pereira'}
print(otro_dicccionario)

otra_forma_dict = dict(total = 55, descuento = True, subtotal = 15)
print(otra_forma_dict)

dicccionario = {"total": 55, 10:"curso de python", 2.0:True}
print(dicccionario)
'''

usuario = {
    'nombre': 'Carlos',
    'edad': 28,
    'curso': 'Curso de python',
    'skills':{
        'programacion': True,
        'base_de_datos': False
    },
    'no medallas': 10
}

'''
print(usuario)
print(usuario['curso'])
print(usuario['skills'])
print(usuario['skills']['base_de_datos'])
'''
diccionario = dict()
print(diccionario)

diccionario['marca'] = 'Mazda'
print(diccionario)
diccionario['marca'] = 'Subaru'
print(diccionario)

nuevo_dict = {'Fernando': 1, 'Juan': 2, 'Jose': 3, 'Maria': 4}
print(nuevo_dict.keys())
print(nuevo_dict.values())

# nuevo_dict.clear()
# print(nuevo_dict)

copia_nuevo_dict = nuevo_dict.copy()
print(nuevo_dict == copia_nuevo_dict)

#version = dict(python = 3.9,zope = 4.5,plone = 2.8)
secuencia = ('python','zope', 'plone')
version = dict.fromkeys(secuencia,'34')
# print(version)

print(version.get('zope'))

