
#(P ^ Q)

'''
P = gana menos dos salarios
Q = vive en el sitio de trabajo
R = la empresa suministra trans completo
S = no vive cerca de la empresa
'''

# (P ^ S) v (-Q ^ S)
# (P ^ (-Q ^ -R ^ S))
# (P ^ S) v -(Q ^ R)
# (P ^ S) ^ (-Q v -R)
# (P ^ -R ^ (-Q v S))

'''
P = anho es divisible por 4
Q = anho es divisible por 100 
R = anho es divisible por 400
'''

# (P ^ -Q ^ R)
# (P ^ -(Q v R))
# P ^ (-Q ^ r)
# (P ^ -Q) v R


'''

Si (1 < 2)
  si se cumple
Fin


Si (1 < 2)
  si se cumple
Sino
  si no se cumple
Fin



if (1 > 2):
    print('se cumple la condición')
else:
    print('no se cumple la condición')
    

horaDelDia = 9

if (horaDelDia >= 12):
    print(horaDelDia, ' P.M.')
else:
    print(horaDelDia, ' A.M.')


num_entero = int(input("digite un numero entero : "))

if num_entero > 0:
    print("el numero es positivo")
if num_entero < 0:
    print("el numero es negativo")
if num_entero == 0:
    print("el numero es cero")
'''

num_len = int(input("ingrese el numero : "))

if (num_len < 0):
    num_len = (num_len * (-1))

'''
if ((num_len >= 1) and (num_len <= 9)):
    print("el número tiene un solo digito")
if ((num_len > 0) and (num_len < 10)):
    print("el número tiene un solo digito")
'''
'''
if (num_len <= 9):
    print("el número tiene un solo digito")
else:
    if (num_len > 9) and (num_len <= 99):
        print("el número tiene dos digitos")
    else:
        if (num_len > 99) and (num_len <= 999):
            print("el número tiene tres digitos")
        else:
            if (num_len > 999) and (num_len <= 9999):
                print("el número tiene cuatro digitos")
            else:
                print("el número tiene mas de cuatro digitos")
'''  

'''
if len(str(num_len)) == 1:
    print("el número tiene un solo digito")
else:
    if len(str(num_len)) == 2:
        print("el número tiene dos digitos")
    else:
        if len(str(num_len)) == 3:
            print("el número tiene tres digitos")
        else:
            if len(str(num_len)) == 4:
                print("el número tiene cuatro digitos")
            else:
                print("el número tiene mas de cuatro digitos") 
'''


if len(str(num_len)) == 1:
    print("el número tiene un solo digito")
elif len(str(num_len)) == 2:
    print("el número tiene dos digitos")
elif len(str(num_len)) == 3:
    print("el número tiene tres digitos")
elif len(str(num_len)) == 4:
    print("el número tiene cuatro digitos")
else:
    print("el número tiene mas de cuatro digitos")
