# funcion all y any

'''
print(all([True,True,True]))
print(all([True,False,True]))

print(any([True,False,True]))
print(any([False,False,False]))

print(all([]))
print(any([]))
'''

info = [ int(input()), input().split(' ')]
print(info)


print('True' 
if all(list(map(lambda x :x >0, list(map(int,info[1] )) )) )
and
any(list(map(lambda x : x[0] == x[1] or x[0] == '5', list(zip(info[1],
list(map(lambda x: x[-1:(len(x)+1)* -1:-1],info[1])) )) )) )
else 'False' )

 
'''
condicion1_1 = list(map(int,info[1] ))
#print(condicion1_1)

condicion1 = all(list(map(lambda x :x >0, list(map(int,info[1] )) )) )
#print(condicion1)


condicion2 = any(list(map(lambda x : x[0] == x[1] or x[0] == '5', list(zip(info[1],
list(map(lambda x: x[-1:(len(x)+1)* -1:-1],info[1])) )) )) )
print(condicion2)
'''

#condicion2_1 = list(zip(info[1],list(map(lambda x: x[-1:(len(x)+1)* -1:-1],info[1])) ))
# print(condicion2_1)

# condicion2_2 = list(map(lambda x: x[-1:(len(x)+1)* -1:-1],info[1]))
# print(condicion2_2)

