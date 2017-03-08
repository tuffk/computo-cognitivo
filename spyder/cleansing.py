# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import Imputer

def eliminamela(t):
    if t > -273:
        return t
    else:
        return np.nan
    
def ceropeamela(v):
    if v >= 0:
        return v
    else:
        return np.nan
    
def limpeamela(x):
    if x > 100000:
        return np.nan
    else:
        return x
    
def misseamela(datos):
    missing = 100 - np.array([
            datos[c].notnull().sum() * 100 / datos.shape[0] for c in datos.columns
                 ])
    return pd.DataFrame({'Column': datos.columns, 'Missing %': missing})


datos = pd.read_csv('/home/tuff/github/computo-cognitivo/files/blade_damage_assessment.csv', index_col='engine_id')

datos.dtypes

num_lineas = len(datos)

columnas = ['t_2', 't_3', 't_4', 'vibrations_2', 'vibrations_4', 'core_speed', 'fan_speed', 'thrust']
clineado = datos[columnas].apply(lambda x: pd.to_numeric(x, errors='coerce'))
clineado.dtypes

for colum in columnas:
    datos[colum] = clineado[colum]
    
datos.dtypes

temperaturas = ['t_1', 't_2', 't_3', 't_4', 't_oil']
datos[temperaturas] = datos[temperaturas].applymap(eliminamela)

velocidades = ['core_speed', 'fan_speed', 'vibrations_2', 'vibrations_4']
datos[velocidades] = datos[velocidades].applymap(ceropeamela)

datos['thrust'] = datos['thrust'].apply(limpeamela)

datos['t_2'] = datos['t_2'].apply(lambda x: x if x < 250 else np.nan)
datos['t_3'] = datos['t_3'].apply(lambda x: x if x < 2000 else np.nan)
datos['t_4'] = datos['t_4'].apply(lambda x: x if x > 0 else np.nan)
datos['vibrations_2'] = datos['vibrations_2'].apply(
            lambda x: x if x < 1.5 else np.nan
        )
datos['vibrations_4'] = datos['vibrations_4'].apply(
            lambda x: x if x < 1.5 else np.nan
        )

#nums3 = datos[(datos['t_3'] == np.nan)]['engine_type'].count()
#nums4 = datos[(datos['t_4'] == np.nan)]['engine_type'].count()

datos['is_B_engine'] = datos['engine_type'].map({'EX-50A': 0, 'EX-50B': 1})
datos['is_failed'] = datos['category'].map({'non-failed': 0, 'failed': 1})
datos.drop(['engine_type', 'category'], axis=1, inplace=True)

perdidos = misseamela(datos)
print(perdidos)

imputado = Imputer(missing_values=np.nan, strategy='mean', axis=1)
for pro in columnas:
    datos[pro] = imputado.fit_transform(datos[pro].values).T
         
perdidos = misseamela(datos)
print(perdidos)

datos.to_csv('/home/tuff/github/computo-cognitivo/files/bdgmclean.csv')

print("success")