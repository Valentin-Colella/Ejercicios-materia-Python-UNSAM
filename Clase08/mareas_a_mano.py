# -*- coding: utf-8 -*-
"""
Created on Tue May 11 19:15:08 2021

@author: HP
"""

import pandas as pd
import numpy as np

df = pd.read_csv('../Data/OBS_SHN_SF-BA.csv',index_col=['Time'], parse_dates=True)
dh = df['12-25-2014':].copy()
delta_t = 0 # tiempo que tarda la marea entre ambos puertos
delta_h = 0 # diferencia de los ceros de escala entre ambos puertos

de = pd.DataFrame(columns = ['error','delta_t','delta_h'])

for delta_t1 in range (-3,0): #estos intervalos los definí en base al gráfico  
    for delta_h1 in np.linspace(0,30,num=500):   
        error = 1/len(dh) * np.sum(np.square((dh['H_SF'].shift(delta_t1)-delta_h1)-
                                             dh['H_BA'])) #fórmula de error cuadrático medio
        de=de.append({'error' : error , 'delta_t' : delta_t1, 
                      'delta_h' : delta_h1},ignore_index=True) #voy llenando un dataframe 
                                                               #con los valores
        
        
a = de.loc[de['error'].idxmin()]  ##Busco el mínimo error 
delta_t = int(a['delta_t'])
delta_h = float(a['delta_h'])

pd.DataFrame([dh['H_SF'].shift(delta_t) - delta_h, dh['H_BA']]).T.plot()




