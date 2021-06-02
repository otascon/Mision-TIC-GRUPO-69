# Funcion filter
# Obtener la cantidad de elementos mayores de 5 de la tupla

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