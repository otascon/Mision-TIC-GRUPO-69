# Funcion reduce

from functools import reduce

'''
lista = [1,2,3,4,5,6,7,8,9]
acumulador = 0

for elemento in lista:
    acumulador += elemento

print(acumulador) 
'''

'''
lista = [1,2,3,4,5,6,7,8,9]
resultado = sum(lista)
print(resultado)
'''

'''
lista = [1,2,3,4,5,6,7,8,9.0]
def funcion_acumular(acumulador = 0, elemento = 0):
    return acumulador + elemento
resultado = reduce(funcion_acumular,lista)
print(resultado)
'''

'''
lista = [1,2,3,4,5,6,7,8,9]
f_acumular = lambda acumulador = 0, elemento = 0 : acumulador + elemento
print(f_acumular(1,1))

resultado = reduce(f_acumular,lista)
print(resultado)
'''

'''
lista = ['Python','Java','Ruby','Elixir']

resultado = reduce(lambda acumulador = '', elemento = '': acumulador + '-' + elemento,lista)
print(resultado)
'''

lista = [1,2,3,4,5,6,7,8,9]
f_acumular = lambda acumulador = 0, elemento = 0 : acumulador + elemento
# print(f_acumular(1,1))
resultado = reduce(f_acumular,lista,10)
print(resultado)