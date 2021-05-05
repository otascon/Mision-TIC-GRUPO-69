'''
import math

+ Suma
- Resta
* Multiplicacion
/ Division
// Division Entera
** Potencia
()
'''


num_1 = 12
num_2 = 15
num_3 = 21

valor = ((num_1 - (num_2 + num_3)) / 100)
potencia = (num_1** num_2)
promedio = ((num_1 + num_2 + num_3)/3)

promedio_sum = (sum((num_1,num_2,num_3))/3)
fun_max = max(num_1,num_2, num_3)
fun_min = min(num_1,num_2,num_3)

print(potencia)
print(promedio_sum)
print(fun_max)
print(fun_min)


# Crear variable de diccionario
var_dict = {"nombre":"Jose","edad":21,"altura":172}
# editar el campo edad del diccionario
var_dict['edad'] = 24
# agregar un nuevo item al diccionario
var_dict['sg_nombre'] = "Maria"
# elimiar un item del diccionario
var_dict.pop('altura')

'''
print("el nombre es " + var_dict["nombre"] + " y su edad es de "+ str(var_dict["edad"]) + " años")
print(var_dict)
'''

var_r1 = range(0,100)
var_r2 = range(20,100)

print(var_r1)
print(var_r2)
print(len(var_r1))
print(len(var_r2))

texto = "Ciclo 1, fundamentos de programación"
print(len(texto))