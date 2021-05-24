'''
    # crear diccionarios -> {}
    d = dict()
    # crear listas -> []
    l = list()
    # crear tuplas -> ()
    t = tuple()
    # crear conjuntos -> {} tener cuidado al declarar
    c = set()
'''

'''
n = 5
while n > 0:
    print(n)
    n = n - 1

print('Termino')
'''

'''
def factorial(num : int)-> int:
    # Inicializar variables
    resultado = 1
    num_actual = 2
    while num_actual <= num:
        # resultado = num_actual * (num_actual + 1)
        resultado = resultado * num_actual
        num_actual += 1  # num_actual = num_actual + 1
        # print(resultado)
    return resultado

print(factorial(1)) 
'''

'''
i = 1
while i > 0:
    print(i)
    i = i + 1
print('Termino')
'''

'''
i = 1
while i != 10:
    print(i)
i += 2
print('Termino!')
'''

'''
promedio, total, contar = 0.0, 0, 0

print('introduzca la nota de un estudiante (-1 para salir) : ')
nota = int(input())
while nota != -1:
    total = total + nota
    contar += 1

    print('introduzca la nota del estudiante (-1 para salir) : ')
    nota = int(input())
promedio = total / contar
print('el promedio de notas de los estudiantes es : ', promedio)
'''

'''
promedio, total, contar = 0.0, 0, 0
nota = 0
while nota != -1:
    print('introduzca la nota del estudiante (-1 para salir) : ')
    nota = int(input())
    if nota != -1:
        total = total + nota
        contar += 1

promedio = total / contar
print('el promedio de notas de los estudiantes es : ', promedio)
'''

'''
promedio, total, contar = 0.0, 0, 0
nota = 0
while nota != -1:
    total = total + nota
    print('introduzca la nota del estudiante (-1 para salir) : ')
    nota = int(input())
    contar += 1

promedio = total / contar
print('el promedio de notas de los estudiantes es : ', promedio)
'''


'''
promedio, total, contar = 0.0, 0, 0
nota = 0
while nota != -1:
    print('introduzca la nota del estudiante (-1 para salir) : ')
    nota = int(input())
    if nota != -1:
        total = total + nota
        contar += 1
else:
    promedio = total / contar
    print('el promedio de notas de los estudiantes es : ', promedio)
'''

'''
variable = 10
while variable > 0:
    print('el valor de la variable es : ', variable)
    variable = variable - 1
    if variable == 5:
        print('finalizacion por break')
        break
'''

'''
variable = 10
while variable > 0:
    variable = variable - 1
    if variable == 5:
        continue
    print('el valor de la variable es : ', variable)
'''


'''
for mi_x in range(0,3):
    print('estamos en la iteracion : '+ str(mi_x))

for j in range(0, 10, 2):
    print('estamos en la iteracion : ', j)

for x in range(10, 0, -2):
    print('estamos en la iteracion : ', x)
'''

'''
oracion = 'Mary entiende bien Python'
frases = oracion.split()
print('la oracion analizada es :', oracion,'.\n')
print(frases)

for palabra in range(len(frases)):
    # for palabra in range(4):
    print("palabra : {}, la frase su posicion es : {}".format(frases[palabra],palabra))
    # print(f"palabra : {frases[palabra]}, la frase su posicion es : {palabra}")
'''

'''
oracion = 'Mary,entiende,bien,Python'
frases = oracion.split(',')
print('la oracion analizada es :', oracion,'.\n')
print(frases)

for palabra in range(len(frases)):
    # for palabra in range(4):
    print("palabra : {}, la frase su posicion es : {}".format(frases[palabra],palabra))
    # print(f"palabra : {frases[palabra]}, la frase su posicion es : {palabra}")
'''

datos_basicos = {
    'nombres': 'Leonardo Jose',
    'apellidos': 'Caballero Garcia',
    'cedula': '1100955988',
    'fecha_nacimiento': '03/12/1980',
    'lugar_nacimiento': 'Bucaramanga',
    'nacionalidad': 'Colombiano',
    'estado_civil': 'Soltero'
}

# clave = datos_basicos.keys()
# print(clave)
# valor = datos_basicos.values()
# print(valor)

'''
cantidad_datos = datos_basicos.items()
print(cantidad_datos)

for clave1,valor1 in cantidad_datos:
    print("clave : {}, valor : {}".format(clave1,valor1))


for argumento in datos_basicos.items():
    print("{}".format(argumento))
'''

frutas = {
    'fresa': 'roja',
    'limon': 'verde',
    'papaya': ' naranja',
    'manzana': 'amarilla',
    'guayaba': 'rosa'
}


for llave in frutas:
    print(llave,' es el color ', frutas[llave])



'''
db_connection = '127.0.0.1','5432','root','nomina'
print(db_connection)

for parametros in db_connection:
    print(parametros)
else:
    print("el comando para postgreSQL es : $ psql -h {} -p {} -u {} -d {}"
    .format(db_connection[0],db_connection[1],db_connection[2],db_connection[3]))
'''