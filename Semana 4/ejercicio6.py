from math import pow

# generar la potencia
print(pow(2,3))

# lista numero
numeroLista = [2,3,4]
# lista potencia
potenciaLista = [3,2,4]

potenciados = map(pow,numeroLista,potenciaLista)
print(list(potenciados))


'''
def calcularPotencia(num,pot):
    resultado = 1
    for x in range(pot):
        resultado = num * resultado
    return resultado

print(calcularPotencia(2,5))

potenciados = list(map(calcularPotencia,numeroLista,potenciaLista))
print(potenciados)
'''