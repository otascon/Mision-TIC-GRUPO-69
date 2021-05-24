nombres = list() # nombres = []
edades = list() # edades = []

for x in range(5):
    nombre = input('digite el nombre de la persona : ')
    nombres.append(nombre)
    edad = int(input('digite la edad de la persona :'))
    edades.append(edad)
    
print('Nombre de las personas mayores de edad \n')
# print(nombres[1], ' su edad es : ', edades[1],'\n')

for x in range(5):
    if edades[x] >= 18:
        print('nombre : ',nombres[x])