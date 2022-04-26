# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 10:05:32 2021

@author: HP
"""

import numpy as np
import matplotlib.pyplot as plt
import random

def merge_sort(lista):
    """Ordena lista mediante el método merge sort.
       Pre: lista debe contener elementos comparables.
       Devuelve: una nueva lista ordenada."""
    comps = 0
    if len(lista) < 2:
        lista_nueva = lista
    else:
        medio = len(lista) // 2
        izq = merge_sort(lista[:medio])[0]
        der = merge_sort(lista[medio:])[0]
        lista_nueva = merge(izq, der)[0]
        comps += merge(izq, der)[1]
    return lista_nueva, comps

def merge(lista3, lista4):
    """Intercala los elementos de lista1 y lista2 de forma ordenada.
       Pre: lista1 y lista2 deben estar ordenadas.
       Devuelve: una lista con los elementos de lista1 y lista2."""
    i, j = 0, 0
    resultado = []
    comps = 0
    while(i < len(lista3) and j < len(lista4)):
        comps +=1
        if (lista3[i] < lista4[j]):
            resultado.append(lista3[i])
            i += 1
        else:
            resultado.append(lista4[j])
            j += 1
    # Agregar lo que falta de una lista
    resultado += lista3[i:]
    resultado += lista4[j:]
    return resultado, comps

def ord_insercion(lista):
    """Ordena una lista de elementos según el método de inserción.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""
    lista2 = lista.copy()
    comp = 0
    comp_total = 0
    for i in range(len(lista2) - 1):
        # Si el elemento de la posición i+1 está desordenado respecto
        # al de la posición i, reubicarlo dentro del segmento [0:i]
        if lista2[i + 1] < lista2[i]:
            comp = reubicar(lista2, i + 1)
        #print("DEBUG: ", lista2)
        comp_total = comp_total + comp
    return comp_total
def reubicar(lista2, p):
    """Reubica al elemento que está en la posición p de la lista
       dentro del segmento [0:p-1].
       Pre: p tiene que ser una posicion válida de lista."""

    v = lista2[p]
    comp = 0
    # Recorrer el segmento [0:p-1] de derecha a izquierda hasta
    # encontrar la posición j tal que lista[j-1] <= v < lista[j].
    j = p
    while j > 0 and v < lista2[j - 1]:
        # Desplazar los elementos hacia la derecha, dejando lugar
        # para insertar el elemento v donde corresponda.
        lista2[j] = lista2[j - 1]
        j -= 1
        comp = comp + 1
    comp = comp + 1
    lista2[j] = v
    return comp
    
def ord_seleccion(lista):
    """Ordena una lista de elementos según el método de selección.
       Pre: los elementos de la lista deben ser comparables.
       Post: la lista está ordenada."""
    lista3 = lista.copy()
    # posición final del segmento a tratar
    n = len(lista3) - 1
    comp_total = 0

    # mientras haya al menos 2 elementos para ordenar
    while n > 0:
        # posición del mayor valor del segmento
        p, comp = buscar_max(lista3, 0, n)
        comp_total = comp_total + comp

        # intercambiar el valor que está en p con el valor que
        # está en la última posición del segmento
        lista3[p], lista3[n] = lista3[n], lista3[p]
        #print("DEBUG: ", p, n, lista3)

        # reducir el segmento en 1
        n = n - 1
    return comp_total

def buscar_max(lista3, a, b):
    """Devuelve la posición del máximo elemento en un segmento de
       lista de elementos comparables.
       La lista no debe ser vacía.
       a y b son las posiciones inicial y final del segmento"""
    comp = 0
    pos_max = a
    for i in range(a + 1, b + 1):
        if lista3[i] > lista3[pos_max]:
            pos_max = i
        comp += 1
    return pos_max, comp

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
        n = n - 1 #Resto uno así no compara con el elemento de la lista
                  #acomodado anteriormente
    return comp
        
def generar_lista(N):
    lista_aleatoria = random.sample(range(1000),N)
    return lista_aleatoria

largos = np.arange(256)
comparaciones_burbujeo = np.zeros(256)
comparaciones_seleccion = np.zeros(256)
comparaciones_insercion = np.zeros(256)
comparaciones_merge = np.zeros(256)

for N in largos:
    lista=generar_lista(N)
    comparaciones_burbujeo[N]=ord_burbujeo(lista)
    comparaciones_seleccion[N]=ord_seleccion(lista)
    comparaciones_insercion[N]=ord_insercion(lista)
    comparaciones_merge[N]=merge_sort(lista)[1]
    
    
plt.plot(largos,comparaciones_burbujeo)
plt.plot(largos,comparaciones_seleccion, linestyle = '--')
plt.plot(largos,comparaciones_insercion)
plt.plot(largos,comparaciones_merge)
plt.xlabel("Largo de la lista")
plt.ylabel("Cantidad de comparaciones")
plt.title("Largo de la lista")
plt.legend(('Burbujeo', 'Seleccion','Insercion','Merge'))
plt.show()
    






