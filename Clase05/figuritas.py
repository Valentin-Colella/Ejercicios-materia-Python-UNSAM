# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 18:00:55 2021

@author: HP
"""

import random
import numpy as np
import matplotlib.pyplot as plt

def crear_album(figus_total):
    album = np.zeros(figus_total)
    return album

def album_incompleto(A):
    if (A[A == 0]).size == 0: ##A[A == 0] guarda todos los ceros de A. Al calcularle el tamaño, si es cero, quiere decir que no hay ceros y por ende el álbum está completo
        return False
    else: 
        return True
    
def comprar_paquete(figus_total, figus_paquete):
    ### creo un paquete de valores entre 0 y el total de fig -1 ya que empiezo a contar desde 0. El álbum que cree va desde 0 a 669 (tiene 670)
    paquete = [random.randint(0,figus_total-1) for i in range(figus_paquete)]   
    return paquete

def cuantos_paquetes(figus_total, figus_paquete):
    A = crear_album(figus_total)   #Creo el album vacío
    cantidad_paq = 0
    while album_incompleto(A):    ##Mientras album_incompleto(album) me retorne True (es decir,esté vacío) se ejecuta el while.
        
        for i in comprar_paquete(figus_total, figus_paquete):      ##"Pego las figuritas en el álbum", según la posicón que tocó
            A[i] = 1
        cantidad_paq += 1      ##Voy sumando la cantidad de paquetes que se compran
    return cantidad_paq


def calcular_historia_figus_pegadas(figus_total, figus_paquete):
    album = crear_album(figus_total)          
    historia_figus_pegadas = [0]
    while album_incompleto(album):       
        paquete = comprar_paquete(figus_total, figus_paquete)
        while paquete:
            album[paquete.pop()-1] = 1
        figus_pegadas = (album>0).sum()
        historia_figus_pegadas.append(figus_pegadas)        
    return historia_figus_pegadas

figus_total = 670
figus_paquete = 5
lista = [cuantos_paquetes(figus_total, figus_paquete) for i in range(100)]
promedio=np.mean(lista)
print(f'\nLa cantidad de paquetes que se compró fue: {int(promedio)}')

plt.plot(calcular_historia_figus_pegadas(figus_total, figus_paquete))
plt.xlabel("Cantidad de paquetes comprados.")
plt.ylabel("Cantidad de figuritas pegadas.")
plt.title("La curva de llenado se desacelera al final")
plt.show()
    
    
