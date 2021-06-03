# Funcion filter
# Obtener la cantidad de elementos mayores de 5 de la tupla

'''
def mayor_a_cinco(elemento):
    return elemento > 5

tupla = (5,2,6,7,8,10,77,55,2,1,30,4,2,3)
print(tupla)
print(len(tupla))

resultado = tuple(filter(mayor_a_cinco,tupla))
print(resultado)
print(len(resultado))

resultado = tuple(filter(lambda elemento : elemento > 5, tupla))
print(resultado)
'''

pares = list()

for i in range(10):
    if i % 2 == 0:
        pares.append(i)

print(pares)

items = [0,1,2,3,4,5,6,7,8,9]
resultado = list(filter(lambda x : x % 2 == 0, items))
print(resultado)