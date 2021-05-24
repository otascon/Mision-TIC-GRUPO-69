
notas = [4,3,5]
alturas = [1.74,1.80,1.60]
dias = ['lunes', 'martes','miercoles']

notas_l = [[4,5],[6,9],[7,3]]

lista = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
# print(lista)
# print(lista[0])
# print(lista[0][0])

'''
for x in range(len(lista[2])):
    print(lista[2][x])
'''

'''
for x in range(len(lista)):
    for j in range(len(lista[x])):
        print(lista[x][j])
'''

'''
lista_dos = [[3,4,8,7,6],[13,76,3,6,9]]
print(lista_dos)

for x in range(len(lista_dos)):
    respuesta_1 = 0 
    for k in range(len(lista_dos[x])):
        respuesta_1 = respuesta_1 + lista_dos[x][k]
    print(respuesta_1)
'''


'''
lista_tres = [[2],[3,4],[12,18,8],[9,5,2,5],[6,7,10,70,4]]

result = 0
for x in range(len(lista_tres)):
    for k in range(len(lista_tres[x])):
        result += lista_tres[x][k]

print(result)
'''

padres = [['Juan','Ana'],['Carlos','Maria'],['Pedro', 'Laura']]
hijos = [['Marcos','Alberto','Silvia'],[],['Oscar']]

print('Lista de Padre, Madre  e hijos')
for x in range(len(padres)):
    print('padre : ', padres[x][0])
    print('madre : ', padres[x][1])
    for k in range(len(hijos[x])):
        print('hijo : ',hijos[x][k])

print('Lista de Padre y cantidad hijos')
for x in range(len(padres)):
    print('Padre : ' + padres[x][0])
    print('Cantidad de hijos : ' + str(len(hijos[x])))
