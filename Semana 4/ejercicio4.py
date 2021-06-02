'''
con_doble_asterisco = lambda ** diccionario : diccionario['a']

dicc = {'a' : 1}
print(con_doble_asterisco(** dicc))
'''

dicc = {'a': 2, 'b': 10, 'c': 5}

resultado = lambda ** diccionario : sum(diccionario.values())
print(resultado(** dicc))