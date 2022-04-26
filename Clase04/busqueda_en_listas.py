# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 16:17:26 2021

@author: HP
"""

def buscar_u_elemento(lista, e):
    pos = -1
    lista1 = []
    for i, r in enumerate(lista):
        if r == e:
            lista1.append(i)
    
    if lista1 == []:
        return pos
    else:
        return max(lista1)
    
def buscar_n_elemento(lista, e):
    n = 0
    for r in lista:
        if r == e:
            n+=1
    return n

def maximo(lista):
    m = lista[0]
    for e in lista:
        if m >= e:
            m = m
        else:
            m = e
    return m
            
def minimo(lista):
    m = lista[0]
    for e in lista:
        if m <= e:
            m = m
        else:
            m = e
    return m
            
print(buscar_u_elemento([1,2,3,2,3,4],4))
print(buscar_n_elemento([1,2,3,2,3,4],3))
print(maximo([-1,-2,-7,-2,-3,-4]))
print(minimo([1,2,7,2,3,4]))
