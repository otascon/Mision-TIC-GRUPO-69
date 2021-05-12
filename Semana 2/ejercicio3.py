'''
+
-
*
/

%

'''

'''
AND = y
OR  = o
'''

'''
== igual
<= menor o igual
>= mayor o igual
< mayor
> menor
!= diferente


num = 10
if num != 10:
    print("el número es diferente")
else:
    print("el número no es diferente")
'''

# print(5 == 5)

'''
n = 11
if n%2 == 0 or n%3 == 0:
    print('correcto')
else:
    print('incorrecto')


if 17 and True:
    print('Correcto')


num = 11
if num%2 == 0:
    print('el numero es par')
else:
    print('el numero es impar')


letra = 'c'
if letra == 'a':
    print('Mal resultado')
elif letra == 'b':
    print('Buen resultado')
elif letra == 'c':
    print('Cerca, pero no es correcto')


x = 8
y = 4
if x == y:
    print('x y y son iguales')
else:
    if x > y:
        print('x es mayor, y es menor')
    else:
        print('y es mayor, x es menor')
'''

# indicar cual el numero mayor, menor y del medio de tres variables

x = 12
y = 9
z = 10

'''
if x > y and x > z:
    print('x es mayor ' + str(x))
else:
    if y > z:
        print('y es mayor ' + str(y))
    else:
        print('z es mayor ' + str(z))
'''

if x > y and x > z:
    # mayor = x
    print(x, ' el número mayor')
if y > x and y > z:
    # mayor = y
    print(y, ' el número mayor')
if z > x and z > y:
    # mayor = z
    print(z, ' el número mayor')

if x < y and x < z:
    # menor = x
    print(x, ' el número menor')
if y < x and y < z:
    # menor = y
    print(y, ' el número menor')
if z < x and z < y:
    # menor = z
    print(z, ' el número menor')

if x > y and x < z or x > z and x < y:
    print(x, 'Es el numero del medio')
if y > x and y < z or y > z and y < x:
    print(y, ' Es el numero del medio')
if z > x and z < y or z > y and z < x:
    print(z, ' El numero del medio')


if x > y and x > z:
    if y > z:
        print(x, ' es el numero mayor')
        print(y, ' es el del medio')
        print(z, ' el numero menor')
    else:
        print(x, ' es el numero mayor')
        print(z, ' el numero del medio')
        print(y, ' el numero menor')
elif y > x and y > z:
    if x > z:
        print(y, ' el numero mayor')
        print(x, ' el numero del medio')
        print(z, ' el numero menor')
    else:
        print(y, ' el numero mayor')
        print(z, ' el numero del medio')
        print(x, ' el numero menor')
elif z > x and z > y:
    if x > y:
        print(z, ' el mnumero mayor')
        print(x, ' el numero del medio')
        print(y, ' el numero menor')
    else:
        print(z, ' el numero mayor')
        print(y, ' el numero del medio')
        print(x, ' el numero menor')

if x > y and x > z and y > z:
    pass