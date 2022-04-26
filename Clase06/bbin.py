# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 18:48:14 2021

@author: HP
"""

def insertar(lista, x, verbose = False):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Si x no está en la lista, lo inserta en la posicón correcta 
    de tal forma que la lista siga ordenada y también devuelve su posición. 
    Si x está en la lista
    devuelve la posicón en la que se encuentra.
    '''
    if verbose:
        print('[DEBUG] izq |der |medio')
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] == x:
            pos = medio     # elemento encontrado!
        if lista[medio] > x:
            der = medio - 1 # descarto mitad derecha
        else:               # if lista[medio] < x:
            izq = medio + 1 # descarto mitad izquierda
    
    pos = izq
    lista1=lista[0:pos]   #Creo una lista con los valores que se encuentran a la izq de la
                          #posicón donde quiero insertar x  
    lista2=lista[pos:len(lista)] #Creo una lista con los valores que se encuentran
                                 #a la derecha de la posicón donde quiero insertar x   
    lista=lista1 + [x] + lista2  #Creo la lista con x insertado
    return lista, pos
    
listaord, pos=insertar([1,2,4,6,300,450,577],15)
print(f'Lista con el elemento x insertado: {listaord}. Este elemento se encuentra en la posición {pos}.')