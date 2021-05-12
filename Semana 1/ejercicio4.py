def suma_var_ini(a,b=21):
    print(a - b)

#suma(24,18)
#suma_var_ini(14,1)
#print(suma(24,12.8))

def imprimirMen():
  print("Grupo 69") 

#imprimirMen()

def imprimirMen_r():
  return "Grupo 69"

# imprimirMen_r()
rta = imprimirMen_r()
print(rta)

# funcion para sumar dos parametros
def suma(var_a,var_b):
  result = var_a + var_b
  return result

print(type(suma(4,7)))

rta = suma(4,7)
#print(rta)


def resta(var_c, var_d):
  result = var_c - var_d
  return result 
 
rta_r = resta(10,35)
#print(rta_r)

def repetirOperacion():
  print(suma(4,8))
  print(suma(7,2))
  print(resta(11,9))
  print(resta(32,1))

repetirOperacion()