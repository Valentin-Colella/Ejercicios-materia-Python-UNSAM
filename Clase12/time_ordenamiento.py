# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 17:49:06 2021

@author: HP
"""
import timeit as tt
import numpy as np
import matplotlib.pyplot as plt
import random

def merge_sort(lista):
    """Ordena lista mediante el método merge sort.
       Pre: lista debe contener elementos comparables.
       Devuelve: una nueva lista ordenada."""
    if len(lista) < 2:
        lista_nueva = lista
    else:
        medio = len(lista) // 2
        izq = merge_sort(lista[:medio])
        der = merge_sort(lista[medio:])
        lista_nueva = merge(izq, der)
    return lista_nueva

def merge(lista3, lista4):
    """Intercala los elementos de lista1 y lista2 de forma ordenada.
       Pre: lista1 y lista2 deben estar ordenadas.
       Devuelve: una lista con los elementos de lista1 y lista2."""
    i, j = 0, 0
    resultado = []

    while(i < len(lista3) and j < len(lista4)):
        if (lista3[i] < lista4[j]):
            resultado.append(lista3[i])
            i += 1
        else:
            resultado.append(lista4[j])
            j += 1

    # Agregar lo que falta de una lista
    resultado += lista3[i:]
    resultado += lista4[j:]

    return resultado

def ord_insercion(lista):
    """Ordena una lista de elementos según el método de inserción.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""
    lista2 = lista.copy()
    for i in range(len(lista2) - 1):
        # Si el elemento de la posición i+1 está desordenado respecto
        # al de la posición i, reubicarlo dentro del segmento [0:i]
        if lista2[i + 1] < lista2[i]:
            reubicar(lista2, i + 1)
        #print("DEBUG: ", lista2)
        
def reubicar(lista2, p):
    """Reubica al elemento que está en la posición p de la lista
       dentro del segmento [0:p-1].
       Pre: p tiene que ser una posicion válida de lista."""

    v = lista2[p]
    # Recorrer el segmento [0:p-1] de derecha a izquierda hasta
    # encontrar la posición j tal que lista[j-1] <= v < lista[j].
    j = p
    while j > 0 and v < lista2[j - 1]:
        # Desplazar los elementos hacia la derecha, dejando lugar
        # para insertar el elemento v donde corresponda.
        lista2[j] = lista2[j - 1]
        j -= 1

    lista2[j] = v


def ord_seleccion(lista):
    """Ordena una lista de elementos según el método de selección.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""
    lista3 = lista.copy()
    # posición final del segmento a tratar
    n = len(lista3) - 1

    # mientras haya al menos 2 elementos para ordenar
    while n > 0:
        # posición del mayor valor del segmento
        p = buscar_max(lista3, 0, n)

        # intercambiar el valor que está en p con el valor que
        # está en la última posición del segmento
        lista3[p], lista3[n] = lista3[n], lista3[p]

        # reducir el segmento en 1
        n = n - 1

def buscar_max(lista3, a, b):
    """Devuelve la posición del máximo elemento en un segmento de
       lista de elementos comparables.
       La lista no debe ser vacía.
       a y b son las posiciones inicial y final del segmento"""

    pos_max = a
    for i in range(a + 1, b + 1):
        if lista3[i] > lista3[pos_max]:
            pos_max = i
    return pos_max

def ord_burbujeo(lista):
    ''' Ordena una lista mediante el método burbujeo'''
    lista1=lista.copy()
    n = len(lista1)
    for b in range(n):
        for a in range(n-1):
            if lista1[a] > lista1[a+1]:
                b = lista1[a]
                lista1[a] = lista1[a+1]
                lista1[a+1] = b
        n = n - 1 #Resto uno así no compara con el elemento de la lista
                  #acomodado anteriormente
        
def generar_listas(Nmax):
    listas = []
    for N in range(1, Nmax+1):
        listas.append(random.sample(range(1000),N))
    return listas

largos = np.arange(256)
tiempos_burbujeo = np.zeros(256)
tiempos_seleccion = np.zeros(256)
tiempos_insercion = np.zeros(256)
tiempos_merge = np.zeros(256)

listas = generar_listas(256)

global lista

for i,lista in enumerate(listas):
     
        # evalúo el método de selección
        # en una copia nueva para cada iteración
        #HAGO LA COPIA DE LAS LISTAS EN CADA METODO.
        tiempo_seleccion = tt.timeit('ord_seleccion(lista)', number = 10,globals = globals())
        # guardo el resultado
        tiempos_seleccion[i]=tiempo_seleccion
        
        tiempo_insercion = tt.timeit('ord_insercion(lista)', number = 10,globals = globals())
        tiempos_insercion[i]=tiempo_insercion
        
        tiempo_burbujeo = tt.timeit('ord_burbujeo(lista)', number = 10,globals = globals())
        tiempos_burbujeo[i]=tiempo_burbujeo
        
        tiempo_merge = tt.timeit('merge_sort(lista.copy())', number = 10,globals = globals())
        tiempos_merge[i]=tiempo_merge
        
        
plt.plot(largos,tiempos_burbujeo)
plt.plot(largos,tiempos_seleccion)
plt.plot(largos,tiempos_insercion)
plt.plot(largos,tiempos_merge)
plt.xlabel("Largo de la lista")
plt.ylabel("Tiempo")
plt.title("Largo de la lista")
plt.legend(('Burbujeo', 'Seleccion','Insercion','Merge'))
plt.show()
        


