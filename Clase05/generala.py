# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 16:37:19 2021

@author: HP
"""

import random
from collections import Counter

def tirar():
    tirada=[]
    for i in range(5):
        tirada.append(random.randint(1,6))
    return tirada

def volver_a_tirar(tirada):
    a = len(tirada)           #Guardo la longitud de la lista recibida (tengo 'a' dados)
    
    tirada = []               #Vacío la lista             
    for i in range(0,a):      #Vuelvo a tirar los dados (tiro 'a' dados)
        tirada.append(random.randint(1,6))
    return tirada

def buscar_mas_repetido(tirada):
    mas_repetido = Counter(tirada).most_common()[0][0]  #Me fijo cual es el mas repetido
    b = tirada.count(mas_repetido)                      #Me fijo cuantas veces se repite
    for i in range(0,b):
        tirada.remove(mas_repetido)                     #Borro el más repetido de la lista
    nuevos_dados = volver_a_tirar(tirada)               #Vuelvo a tirar los otros dados
    for i in range(0,b):
        nuevos_dados.append(mas_repetido)               #Genero una lista con los nuevos dados y los mas repetidos que obtuve antes
    return nuevos_dados

def es_generala(tirada):
    a=tirada.count(tirada[0])                          #Me fijo si hice obtuve generala
    if a==5:
        return True
    else:                                            #Si no obtuve generala, vuelvo a tirar
        nuevos_dados = buscar_mas_repetido(tirada) 
        b=nuevos_dados.count(nuevos_dados[4])                 #Me fijo si hice generala
        if b==5:
            return True  
        else:                                      #Si no hice, vuelvo a tirar
            nuevos_dadoss = buscar_mas_repetido(nuevos_dados)  
            c=nuevos_dadoss.count(nuevos_dadoss[4]) 
            if c==5:
                return True
            else:
                return False
                      
N=1000000
G = sum([es_generala(tirar()) for i in range(N)])
prob = G/N
print(f'Tiré {N} veces, de las cuales {G} saqué generala servida.')
print(f'Podemos estimar la probabilidad de sacar generala servida mediante {prob:.6f}.')