# libreria pandas - Series

import pandas as pd

'''
s = pd.Series([7,5,3])
print(s)
s= pd.Series([7,5,3], index = ['Ene','Feb','Mar'])
print(s)
'''

# Utilizando un diccionario

'''
d = {'Ene':7,'Feb':5,'Mar':2}
s = pd.Series(d)
print(s)
s_i = pd.Series(d, index=['Abr','Mar','Feb','Ene'], dtype=int)
print(s_i)
'''

# Utilizando un escalar

s = pd.Series(7, index=['Ene','Feb','Mar'])

print(s)
