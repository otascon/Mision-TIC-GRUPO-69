# libreria matplotlib - pyplot

import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame(
    {
        'nombre':['john','mary','peter','jeff','bill','lisa','jose'],
        'edad':[23,78,22,19,45,33,20],
        'genero':['M','F','M','M','M','F','M'],
        'estado': ['california','dc','california','dc','california','texas','texas'],
        'num_hijos': [2,0,0,3,2,1,4],
        'num_mascotas': [5,1,0,5,2,2,3]
    }
)

print(df.head())

df.plot(kind='scatter',x ='num_hijos',y = 'num_mascotas', color = 'red')
plt.show()

df.plot(kind='bar',x='nombre',y = 'edad', color = 'blue')
plt.show()