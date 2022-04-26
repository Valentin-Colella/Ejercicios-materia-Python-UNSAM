# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 17:52:24 2021

@author: HP
"""

def bbinaria_rec(lista, e):
    if len(lista) == 0:
        res = False
    elif len(lista) == 1:
        res = lista[0] == e
    else:
        medio = len(lista)//2
        if lista[medio] > e:
            a = bbinaria_rec(lista[0:medio],e) #descarto mitad derecha
            res = a 
        else:               # if lista[medio] < x:
          a = bbinaria_rec(lista[medio:lista[len(lista)-1]],e) # descarto mitad izquierda
          res = a
    
    return res


#lista_1=[1,2,3,4,5]
#print(bbinaria_rec(lista_1,4))