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


'''
lista = ['h','o','l','a', 123, (1,2),{'id': 2009855}]
tupla = tuple(lista)
print(tupla)

lista_c = ['h','o','l','a',1,1,2]
conjunto = set(lista_c)
print(conjunto)
'''

# conversión de tuplas

'''
tupla = 'g','r','u','p','o',' ','6','9'
cadena = ''.join(tupla)
print(cadena)
'''

'''
tupla = ('hola',1234,'grupo')
lista = list(tupla)
print(lista)
'''

'''
tupla = ('hola',12345,'grupo', 'hola')
conjunto = set(tupla)
print(conjunto)

try:
    cadena = ''.join(tupla)
    print(cadena)
except:
    print('Error concatenar tipo de variables diferente string')


convertirCadena = ''
for valor in tupla:
    convertirCadena = convertirCadena + str(valor) 
print(convertirCadena)

for posicion in range(len(tupla)):
    convertirCadena += str(tupla[posicion])
print(convertirCadena)
'''

# Manejo de condicionales
'''
x = 7

if x > 8:
    pass
elif x < 7:
    pass
else:
    if x == 0:
        pass
    elif x > 7:
        pass
    else:
        print('ninguna cumple')
'''

# Conversión de conjunto

'''
conjunto = {'g','r','u','p','o'}
cadena = ''.join(conjunto)
print(cadena)
'''

'''
conjunto = {'h','o','l','a'}
tupla = tuple(conjunto)
print(tupla)
'''

'''
conjunto = {'h','o','l','a'}
lista = list(conjunto)
print(lista)
'''

# conversión de diccionarios

'''
cadena = 'grupo_69'
diccionario1 = dict(zip(range(len(cadena)),cadena))
print(diccionario1)

diccionario2 = dict(zip(cadena,range(len(cadena))))
print(diccionario2)
'''
'''
lista = ['h','o','l','a']
dic_lista = dict(zip(range(len(lista)),lista))
print(dic_lista)
'''

'''
tupla = ('h','o','l','a')
dic_tupla = dict(zip(range(len(tupla)),tupla))
print(dic_tupla)
'''

'''
conjunto = {'h','o','l','a'}
dic_conjunto = dict(zip(range(len(conjunto)),conjunto))
print(dic_conjunto)
'''

'''
l_valor = {'uno', 'dos', 'tres', ' cuatro', 'cinco','seis'}
l_llave = [1,2,3,4,5]

diccionario = dict(zip(l_llave,l_valor))
print(diccionario)
'''

'''
diccionario = {0:'h',1:'o',2:'l',3: '1'}
cadena = ''.join(diccionario.values())
print(cadena)
'''

'''
diccionario = {0:'h',1:'o',2:'l',3: '1'}

tuplaLlave = tuple(diccionario.keys())
tuplaValor = tuple(diccionario.values())
tuplaItems = tuple(diccionario.items())
print(tuplaLlave)
print(tuplaValor)
print(tuplaItems)
'''

'''
diccionario = {0:'h',1:'o',2:'l',3: '1'}

listaLlave = list(diccionario.keys())
listaValor = list(diccionario.values())
listaItems = list(diccionario.items())
print(listaLlave)
print(listaValor)
print(listaItems)
'''

'''
diccionario = {0:'h',1:'o',2:'l',3: 'a',4:'a'}

conjuntoLlave = set(diccionario.keys())
conjuntoValor = set(diccionario.values())
conjuntoItems = set(diccionario.items())
print(conjuntoLlave)
print(conjuntoValor)
print(conjuntoItems)
'''

# tuple() 
# list()
# set()
# dict()

diccionario = {0:'h',1:'o',2:'l',3: 'a',4:'a'}
print(diccionario.items())

l_llave = [1,2,3,4,5]
miLista = list(zip(l_llave,diccionario.values()))
print(miLista)

miTupla = tuple(zip(l_llave,diccionario.keys()))
print(miTupla)

miConjunto = set(zip(l_llave,diccionario.values()))
print(miConjunto)
