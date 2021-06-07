# Lista de comprensiones

mi_diccionario = dict()

for y in range(3,11):
    mi_diccionario[(y,y**3)] = []
    for x in range(4,31,2):
        if x%y == 0:
            mi_diccionario[(y,y**3)].append(x**2)

print(mi_diccionario)
# print(mi_diccionario.keys())

mi_diccionario_c = { (x,x**3) : [ y**2 for y in range(4,31,2) if y%x == 0] for x in range(3,11) }
print('\n',mi_diccionario_c)

resultado = all(list(map(lambda x : x[0] == x[1],
list(zip(mi_diccionario.values(),mi_diccionario_c.values())))))

if mi_diccionario == mi_diccionario:
    print('True')

# print(resultado)

#print( [y**2 for y in range(4,31,2)] )

# Generar elementos de la lista divisible por 3
# print( [y**2 for y in range(4,31,2) if y%3 == 0] )

'''
# Lista de numeros cuadrados
lista = [x**2 for x in range(11)]
print(lista)
'''