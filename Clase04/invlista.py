# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 17:23:20 2021

@author: HP
"""

def invertir_lista(lista):
    invertida = []
    i = len(lista) - 1
    while i>=0:
        invertida.append(lista[i])
        i-=1
    return invertida

for i in (['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel'],[1,2,3,4,5]):
    invertida = invertir_lista(i)
    print(f'Lista original:{i}. Lista invertida:{invertida}')
    print('\n')

'''Resultado obtenido al ejecutar:
    Lista original:['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel']. Lista invertida:['San Miguel', 'San Fernando', 'Santiago', 'Rosario', 'Bogotá']
    
    Con números: Lista original:[1, 2, 3, 4, 5]. Lista invertida:[5, 4, 3, 2, 1] '''