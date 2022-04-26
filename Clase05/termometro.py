# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 09:34:18 2021

@author: HP
"""
import random
import numpy as np
n=999
medidas = []
for i in range(n):
    error=random.normalvariate(0,0.2)
    medida = 37.5 + error
    medidas.append(medida)
medidas = np.array(medidas)    


print(f'Valor máximo obtenido {max(medidas):.2f}')
print(f'Valor mínimo obtenido: {min(medidas):.2f}')
print(f'Promedio: {(sum(medidas)/n):.2f}')
medidas.sort()
print(f'La mediana es: {medidas[50]:.2f}')
np.save('../Data/Temperaturas', medidas)

