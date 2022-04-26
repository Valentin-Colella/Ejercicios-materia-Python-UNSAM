# -*- coding: utf-8 -*-
"""
Created on Wed Apr 28 13:34:40 2021

@author: HP
"""

import numpy as np
import matplotlib.pyplot as plt

def randomwalk(largo):
    pasos=np.random.randint (-1,2,largo)    
    return pasos.cumsum()

N = 100000
maximos=[]
conjunto_pasos=[]
for i in range(0,12):
    a = randomwalk(N)
    #Guardo el máximo valor de cada caminata (en módulo)
    maximo = max(abs(a))
    #Guardo los máximos en una lista
    maximos.append(maximo)
    #Guardo todas las caminatas
    conjunto_pasos.append(a)
    
plt.subplot(2, 1, 1) 
#Grafico las caminatas
for i in conjunto_pasos:
    plt.plot(i)
    plt.xticks([])
    plt.yticks([-500,0,500])
    plt.title('12 caminatas al azar')
plt.show()
    

for i in conjunto_pasos:
    #Me fijo cual es la caminata que llega a un valor mas alejado del 0
    if max(abs(i))==max(maximos):
        mas_alejado = i
    #Me fijo cual es la que menos se aleja
    elif max(abs(i))==min(maximos):
        mas_cercano = i
    
#Grafico el mas alejado
plt.subplot(2, 2, 3)
plt.plot(mas_alejado)
plt.yticks([-500,0,500])
plt.xticks([])
plt.title('Caminata que mas se aleja')

#Grafico el mas cercano
plt.subplot(2, 2, 4)
plt.plot(mas_cercano)
plt.yticks([-500,0,500])
plt.xticks([])  
plt.title('Caminata que menos se aleja')

    
    


    
    
    
    