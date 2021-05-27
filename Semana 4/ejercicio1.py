'''
cadena = 'grupo_69'
lista = list(cadena)
print(lista)
'''

'''
cadena = 'hola'
cadena2 = 'adios'
num = 15
tupla1 = tuple(cadena)
tuplaGeneral = (tupla1,num,tuple(cadena2))
print(tuplaGeneral)
'''

'''
cadena = 'hhola'
cadena2 = '53683538224'
print(set(cadena))
print(set(cadena2))


convertir_cadena = list(cadena2)
lista = list()
for x in convertir_cadena:
    lista.append(int(x))

print(set(lista))
'''

'''
cadena = 'hola'
tupla = tuple(cadena)

try:
    tupla[0] = 'L'
    print(tupla)
except:
    print('el elemento de una tupla no puede ser modificado')

lista = list(cadena)
lista[0] = 'L'
print(lista)
'''


convertir_cadena = ''
lista = ['h','o','l','a',(1,2)]

try:
    convertir_cadena = convertir_cadena.join(lista)
    print(convertir_cadena)
except:
    print('Error concatenar elemento de tipo datos diferentes ha string')

cadena2= ''
for elemento in lista:
    cadena2 = cadena2 + str(elemento)

print(cadena2)

'''
lista = ['h','o','l','a', 123, (1,2),{'id': 2009855}]
tupla = tuple(lista)
print(tupla)

lista_c = ['h','o','l','a',1,1,2]
conjunto = set(lista_c)
print(conjunto)
'''


