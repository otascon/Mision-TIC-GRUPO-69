# Funciones anonimas (lambda)

'''
suma = lambda var1 = 0,var2 = 0 : var1 + var2
# print(suma(8,17))
operacion = lambda operacion, var1 = 0, var2 = 0 : operacion(var1,var2)

resultado = operacion(suma,37,57)
print(resultado)
'''

'''
sin_parametro = lambda :True
# print(sin_parametro() == True) 

con_valores = lambda val1, val2 = 0, val3 = 0 : val1 + val2 + val3
# print(con_valores(10,20,30))
'''

con_asterisco = lambda * args : args[0]
lista = [5,6,8,7,9]
# print(con_asterisco(* lista))

def suma (* args):
    resultado = 0
    for i in args:
        resultado = resultado + i
    return resultado

# print(suma(* lista))

tupla = 5,6,7,8,9
con_asterisco_suma = lambda funcion, * args : funcion(* args) 
# print(con_asterisco_suma(suma,* tupla))


def sumar(* args):
    return args[0] + args[1]

lista = [1,2,3,4]
print(sumar(*lista))
