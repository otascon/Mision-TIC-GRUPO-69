def consultar_nombre_genero(letra_genero): 
    pass # operación nula

type(consultar_nombre_genero)
consultar_nombre_genero("M")

print(consultar_nombre_genero("M"))

def multiplicar(var_x : int, var_y : int):
    resultado = (var_x * var_y)
    return resultado

print(multiplicar(4,3.4))
print(type(multiplicar(4, 3.4)))

# crear variable de tipo diccionario
info_persona = {
    'nombre':'',
    'pr_apellido':'',
    'sg_apellido':''
}

# modificar valores del la variable diccionario
info_persona['nombre'] = input("ingrese el nombre")
info_persona['pr_apellido'] = input("ingrese el primer apellido")
info_persona['sg_apellido'] = input("ingrese el segundo apellido")

def mostrar_info_persona(var_dict):
    resultado = var_dict['nombre'] + " " + var_dict['pr_apellido'] + " " + var_dict['sg_apellido']
    return resultados
    

print("el nombre completo de la personas es : " + mostrar_info_persona(info_persona))





