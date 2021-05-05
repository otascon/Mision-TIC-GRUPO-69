nota1 = 3.6
nota2 = 4
nota3 = 4.7
nota4 = 2.3
nota5 = 2

promedio = ((nota1 + nota2 + nota3 + nota4 + nota5) / 5)
promedio_s = sum((nota1,nota2,nota3,nota4,nota5)) / 5
#print(promedio_s)

def calcular_promedio(n1,n2,n3,n4,n5):
    resultado = ((n1 + n2 + n3 + n4 + n5) / 5)
    resultado = round(resultado,1)
    # print(resultado)
    return resultado

print(calcular_promedio(nota1, nota2, nota3, nota4, nota5))
rta = calcular_promedio(nota1, nota2, nota3, nota4, nota5)
#print(type(rta))

def calcular_promedio_g(notas_g):
    resultado = sum(notas_g) / len(notas_g)
    resultado = round(resultado,2)
    return resultado 

# print(type(notas))

notas_e1 = (3.6,4,4.7,2.3,2)
print(calcular_promedio_g(notas_e1))

notas_e2 = (4,2.5,3,1)
print(calcular_promedio_g(notas_e2))

notas_e3 = (3,5,3.7,4.5,3,8,4.4)
print(calcular_promedio_g(notas_e3))

# crear función para calcular el promedio de 5 notas
def calcular_promedio_osc(n1,n2,n3,n4,n5):
    res_total = sum((n1,n2,n3,n4,n5))
    res_contar = len((n1,n2,n3,n4,n5))
    res_pro = res_total / res_contar
    # print(res_contar)
    return res_pro

print(calcular_promedio_osc(4, 3, 2.4, 1, 3))
