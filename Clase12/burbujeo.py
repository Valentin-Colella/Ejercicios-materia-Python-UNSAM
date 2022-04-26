# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 16:03:15 2021

@author: HP
"""

def ord_burbujeo(lista):
    lista1=lista.copy()
    comp = 0
    n = len(lista1)
    for b in range(n):
        for a in range(n-1):
            if lista1[a] > lista1[a+1]:
                b = lista1[a]
                lista1[a] = lista1[a+1]
                lista1[a+1] = b
            comp+=1
        n = n - 1#Resto uno así no compara con el elemento de la lista
                  #acomodado anteriormente
    return comp

        
lista_1 = [3,0,1,2]
print(ord_burbujeo(lista_1))

        