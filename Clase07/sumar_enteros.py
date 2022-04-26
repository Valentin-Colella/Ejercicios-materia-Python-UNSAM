# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 15:54:13 2021

@author: HP
"""
#%%
def sumar_enteros(desde, hasta):
    '''Calcula la sumatoria de los números entre desde y hasta.
       Si hasta < desde, entonces devuelve cero.

    Pre: desde y hasta son números enteros
    Pos: Se devuelve el valor de sumar todos los números del intervalo
        [desde, hasta]. Si el intervalo es vacío se devuelve 0
    '''
    if hasta<desde:
        return 0
    a=0
    for i in range(desde,hasta+1):
        a = a + i
    return a


suma=sumar_enteros(20,30)
print(suma)


#%%
def sumar_enteros(desde, hasta):
    '''Calcula la sumatoria de los números entre desde y hasta.
       Si hasta < desde, entonces devuelve cero.

    Pre: desde y hasta son números enteros
    Pos: Se devuelve el valor de sumar todos los números del intervalo
        [desde, hasta]. Si el intervalo es vacío se devuelve 0
    '''
    
    T=((desde-1)*(desde))/2  ##Calculo la suma desde 1 hasta el número anterior a 'desde'
    T1=(hasta*(hasta+1))/2   ##Calculo la suma desde 1 hasta el número 'hasta'
    resultado=T1-T
    return resultado

suma=sumar_enteros(20,30)
print(suma)
    
    