# Lista de compresiones

lista_vocales = ['A','E','I','O','U']
lista_nombres = ['Juan','Alejandro','Fernando','Angel','Omar','Ana','Fredy',
'Elias']

lista_nueva_nombre = [l_nombre for l_nombre in lista_nombres if l_nombre[0] in lista_vocales]
print(lista_nueva_nombre)