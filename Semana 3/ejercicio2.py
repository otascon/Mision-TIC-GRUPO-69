'''
t = 'a','b','c','d','e'
print(t)

t = ('esto es una cadena','b','c','d')
print(t)
'''

'''
t = tuple('lupines')
print(t)
print(t[3:6])

# t[0] = 'A'

print((0,1,200000) < (0,3,4))
'''

txt = 'but soft what ligth windows break'
palabra = txt.split()
# print(palabra)
# print(type(palabra))

l = list() # es igual l = []
listas = list()
for subcadena in palabra:
    l.append((len(subcadena),subcadena))
    listas.append((0,len(subcadena),subcadena))
'''
print(l)

l.sort(reverse=True)
print(l)

res = list()
res_num = list()
for num_leg, palabra in l:
    res.append(palabra)
    res_num.append(num_leg)
print(res)
print(res_num)
'''
res = list()
for num_i,num_f,palabra in listas:
    res.append((num_i,num_f))

print(res)




