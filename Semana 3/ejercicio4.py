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