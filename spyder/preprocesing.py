#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  7 16:37:06 2017

@author: tuff
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from scipy.special import expit

df = pd.read_csv('/home/tuff/github/computo-cognitivo/files/bdgmclean.csv')

grouped = df.groupby('engine_id')

avg_data = grouped.aggregate(np.mean)

avg_data['flight_count'] = grouped.count()['flight_id']
totflight = avg_data['flight_count'].sum()

df_no_duplicates = df.drop_duplicates('engine_id')
df_no_duplicates.reset_index(inplace=True)
df_no_duplicates.set_index('engine_id',inplace=True)
avg_data['customer'] = df_no_duplicates['customer']

avg_data.drop('flight_id',axis=1,inplace=True)
numerical_feature = ['t_1','t_2','t_3','t_4','t_oil','p_oil','vibrations_2','vibrations_4',
                     'core_speed','fan_speed','thrust','flight_count']

scaler = StandardScaler()
avg_data.loc[:,numerical_feature] = scaler.fit_transform(avg_data[numerical_feature])
avg_data.loc[:,numerical_feature] = expit(avg_data[numerical_feature].values)
avg_data[numerical_feature].boxplot()
print("numero de vuelos: " + totflight)