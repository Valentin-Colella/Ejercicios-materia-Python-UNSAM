# -*- coding: utf-8 -*-
"""
Created on Tue Apr 27 16:46:18 2021

@author: HP
"""
#%%
def valor_absoluto(n):
    '''Calcula el valor absoluto de un número
       Pre: la función tiene que recibir un número (int/float)
       Pos: devuelve su valor absoluto '''
    if n >= 0:
        return n
    else:
        return -n

#%%
def suma_pares(l):
    '''Suma los números pares de una lista
    Pre: l es una lista de números
    Pos: Se devuelve la suma de los números pares que se encuentran en la lista
    '''
    res = 0
    for e in l:
        if e % 2 ==0:
            res += e
        else:
            res += 0

    return res
    #El invariante de ciclo es que 'res' contenga la suma de los elementos pares recorridos
    #en la lista, por eso comienza en cero.
#%%
def veces(a, b):
    '''Suma el número 'a', 'b' veces.
       Pre: recibir dos números, el primero es el número que quiero sumar y el segundo
       la cantidad de veces que quiero hacerlo, éste tiene que ser positivo.
       Pos: número 'a' sumado 'b' veces
         '''
    res = 0
    nb = b
    while nb != 0:
        #print(nb * a + res)
        res += a
        nb -= 1
    return res
    
    #El invariante de ciclo es que 'res' contiene la suma de 'a' en todo momento.
#%%
def collatz(n):
    '''Se aplica la conjetura de Collatz a un número 'n'
       Pre: cualquier número entero positivo
       Pos: cantidad de pasos necesarios para llegar a 1'''
    res = 1

    while n!=1:
        if n % 2 == 0:
            n = n//2
        else:
            n = 3 * n + 1
        res += 1

    return res
    #El invariante de ciclo es que 'res' contiene la cantidad de veces que 
    #se ejecutó una operación (ya sea dividir el número por dos o multiplicarlo
    #por 3 y sumarle 1)

