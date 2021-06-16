# libreria de pandas - libreria numpy

import numpy as np
import pandas as pd

unidad_datos = np.array([
    [2,5,3,2],
    [4,6,7,2],
    [3,2,4,1]
])

'''
unidades = pd.DataFrame(unidad_datos)
print(unidades)
'''

unidades = pd.DataFrame(unidad_datos, index=[2015,2016,2017], 
    columns=['Ag','Au','Cu','Pt'])
print(unidades)


unidad_2015 = {'Ag':2,'Au':5,'Cu':3,'Pt':2}
unidad_2016 = {'Ag':4,'Au':6,'Cu':7,'Pt':2}
unidad_2017 = {'Ag':3,'Au':2,'Cu':4,'Pt':1}

unidades = pd.DataFrame([unidad_2015,unidad_2016,unidad_2017],
index=[2015,2016,2017])

print(unidades)