''' 
  contador = contador + 1
  contador += 1
  acumulador = acumulador + variable
  acumulador += variable
'''


'''
lista = [1, 2.5, "Devcode", [5,6], 4]
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])
# print(lista[4])
print(lista[3][0])
print(lista[3][1])
print('Hicimos este cambio ->', lista[1:4])
print(lista[1:6])
print(lista[1:5:2])
'''



'''
nombre = 'Pepe'
edad = 25
lista = [nombre,edad]
print(lista)
nombre += 'Juan'
print(lista)
print(type(lista[0]))
'''

'''
nombres = ['Juan', 'Luis']
edades = [24,21]
lista = [nombres,edades]
print(lista)

nombres += ['Cristina']

print(nombres)
print(type(lista[0]))
'''


versiones_iphone = [5,6,7,8]
versiones_iphone.append(6)
# print(versiones_iphone)

# print(versiones_iphone.count(7))
versiones_iphone.extend([10])
# print(versiones_iphone)

versiones_iphone += [10]
# print(versiones_iphone)

versiones_iphone.extend(range(3,15))
print(versiones_iphone)

# print(versiones_iphone.index(10))
# print(versiones_iphone.index(10, 10))

try:
  print(versiones_iphone.index(1))
except:
  print('el valor no esta en la lista')

versiones_iphone.insert(7,1)
versiones_iphone.insert(8,2)
#print(versiones_iphone)

versiones_iphone.remove(10)

print(versiones_iphone)

versiones_iphone.reverse()
print(versiones_iphone)

versiones_iphone.sort()
print(versiones_iphone)

