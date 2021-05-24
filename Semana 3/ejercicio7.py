'''
cadena = 'Este es un atributo '
cadena_nueva = cadena + 'nuevo'
print('Flujo : ', cadena_nueva)
print(cadena_nueva[0:4])
'''

itinerario = [['Santa Marta',1],['Cartagena',2],['San Andres', 4]]
itinerario.append(['Provivencia',2])
print(itinerario)
itinerario.pop(1)
itinerario[0][1] += 1

itinerario[0], itinerario [-1] = itinerario[-1], itinerario[0]
print(itinerario)


for i,lista in itinerario:
    print(i,lista)


for i,destino in enumerate(itinerario):
    print('posición :', i)
    print(destino)
