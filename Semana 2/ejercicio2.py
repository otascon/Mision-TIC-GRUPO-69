def testNumero ():
    entero = int(input("ingrese el número : "))
    resultado = ""
    if entero == 0:
        resultado = "no se puede ingresar el cero"
    if entero > 0:
        if len(str(entero)) == 2:
            resultado = "el numero tiene dos digitos positivos"
        else:
            resultado = "tiene mas o menos de dos digitos positivos"
    if entero < 0:
        # entero = entero * (-1)
        # if len(str(entero)) == 4:
        if len(str(entero)) -1 == 3:
            resultado = "el número tiene tres digitos negativos"
        else:
            resultado = "tiene mas o menos de tres digitos negativos"
    return resultado 
   

print(testNumero())