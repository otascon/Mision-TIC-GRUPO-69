# Obtener el cuadrado de cada elemento de la lista

'''
def cuadrado(numero):
    return numero * numero

lista = [1,2,3,4,5,6,7,8,9,10]
nuevaLista = list(map(cuadrado,lista))
print(nuevaLista)
'''

'''
lista2 = [11,12,13,14,15]
listaLambda = list(map(lambda num : num * num,lista2))

print(listaLambda)
'''

def multi_por_dos(num):
    return num * 2

lista = [12,13,14,15,16,15,16]
print(lista)

nuevaLista = list(map(multi_por_dos,lista))
print(nuevaLista)

listaLambda = list(map(lambda num : num * 2, lista))
print(listaLambda)
