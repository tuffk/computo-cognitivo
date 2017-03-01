# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pandas as pd
from sklearn.preprocessing import Imputer

df = pd.read_casv('/home/tuff/github/computo-cognitivo/files/blade_damage_assessment.csv', index_col='engine_id')

problemcols = ['t_3','t_4','vibrations_2','vibrations_4', 'core_speed']
sf = df[problemcols].apply(lambda x: pd.to_numeric(x,errors='coerce'))

for pc in problemcols:
    df[pc] = sf[problemcols]

def eliminatetemps(t):
    if t > -273.15:
        return t
    else:
        return np.nan

tempcols=['t_1','t_2','t_3','t_4','t_oil']

df[tempcols] = df[tempcols].applymap(eliminatetemps)

def eliminatevibs (v):
    if v > 0:
        return v
    else:
        return np.nan

vibsspeeds = ['fan_speed','core_speed','vibrations_2','vibrations_4','thrust']

df[vibsspeeds] = df[vibsspeeds].applymap(eliminatevibs)

def cleanThrust (x):
    if x > 100000:
        return np.nan
    else:
        return x

df[vibsspeeds] = df[vibsspeeds].applymap(cleanThrust)

df['t_2'] = df['t_2'].apply(lambda x: x if x < 250 else np.nan)
df['t_3'] = df['t_3'].apply(lambda x: x if x < 2000 else np.nan)
df['t_4'] = df['t_4'].apply(lambda x: x if x > 0 else np.nan)
df['vibrations_2'] = df['vibrations_2'].apply(lambda x: x if x < 1.5 else np.nan)
df['vibrations_4'] = df['vibrations_4'].apply(lambda x: x if x < 1.5 else np.nan)


print(df[(df['t_2'] == np.nan)].count)


df['is_B_engine'] = df['engine_type'].map({'EX-50A' : 0, 'EX-50B': 1})
df['is_failed'] = df['category'].map({'non-failed': 0, 'failed': 1})
df.drop(['engine_type', 'category'], axis=1,inplace=True)

def missings (df):
    missing = 100 - np.array([df[c].notnull().sum*100.0 / df.shape[0] for c in df.columns])
    return pd.DataFrame({'Column': df.columns, 'missing %' : missing})

missing_data = missings(df)
print (missing_data)

imp = Imputer(missing_data = np.nan, strategy='mean',axis=1)
for prob in problemcols:
    df[prob] = imp.fit_transform(df[prob].values).T

df.to_csv('/home/tuff/github/computo-cognitivo/files/bdgmclean.csv')