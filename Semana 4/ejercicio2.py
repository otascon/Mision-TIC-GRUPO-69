# Envoltura de funciones

'''
def suma(val1 = 0,val2 = 0):
    return val1 + val2
print(suma())

# Asignar funcion a una variable
funcion_suma = suma

# funcion puede retornar otra funcion
def operacion(funcion,val1= 0, val2 = 0):
    return funcion(val1,val2)

# funcion utilizada como parametro de otra funcion
resultado = operacion(funcion_suma,34,87)
print(resultado)
'''

'''
def crear_funcion(operador):
    if operador == '+':
        def suma(val1 = 0,val2 = 0):
            return val1 + val2
        return suma
    elif operador == '-':
        def resta(val1 = 0,val2 = 0):
            return val1 - val2
        return resta

def operacion(funcion,val1 = 0,val2 = 0):
    return funcion(val1,val2)

funcion_suma = crear_funcion('+')
resultado = operacion(funcion_suma,45,93)
print(resultado)

funcion_resta = crear_funcion('-')
resultado = operacion(funcion_resta,67,28)
print(resultado)
'''