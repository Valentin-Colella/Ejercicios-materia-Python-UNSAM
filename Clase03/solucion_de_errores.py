# -*- coding: utf-8 -*-
#solucion_de_errores.py
#Ejercicios de errores en el código
#%%
#Ejercicio 3.1. Función tiene_a()
#Comentario: Primero, no se fija en todas las letras de la palabra ya que solo retorna
#            el valor que tiene la primer letra y segundo solo funciona para 'a' minúsucla  
# Lo corregí agregando como condición que también se fije si está la 'A' y que
# recorra todas las letras HASTA que encuentre una 'a' o 'A', sino, devuelve False
# Código corregido: 
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a' or expresion[i] == 'A':
            return True
        i += 1
    return False

print(tiene_a('UNSAM 2020'))
print(tiene_a('abracadabra'))
print(tiene_a('La novela 1984 de George Orwell'))


#%%
#Ejercicio 3.2. Función tiene_a()
#Comentario: Al no poner los dos puntos (:) al final de las líneas donde se define la funcion,
#            de if, while, hay error de sintaxis. También, al escribir False como Falso.
#Código corregido: 
    
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i<n:
        if expresion[i] == 'a' or expresion[i] == 'A':
            return True
        i += 1
    return False

print(tiene_a('UNSAM 2020'))
print(tiene_a('La novela 1984 de George Orwell'))


#%%
#Ejercicio 3.3. Función tiene_uno()
#Comentario: A los objetos de tipo int no se les puede aplicar la funcion len()
#Entonces, hay que definir a 1984 como un string poniendolo entre ''.
#Código corregido: 
def tiene_uno(expresion):
    n = len(expresion)
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if expresion[i] == '1':
            tiene = True
        i += 1
    return tiene


print(tiene_uno('UNSAM 2020'))
print(tiene_uno('La novela 1984 de George Orwell'))
print(tiene_uno('1984'))

#%%
#Ejercicio 3.4: funcion suma(a,b)
#Comentario: Las variables sólo son válidas en la estructura que se definan.
#            Por eso cuando se modifica el valor de 'c' en la función, y se imprime 
#            el resultado fuera de la función, c no tiene valor.
#La solución fue retornar el valor de 'c'.
#Código: 
def suma(a,b):
    c = a + b
    return c
a = 2
b = 3
c = suma(a,b)
print(f"La suma da {a} + {b} = {c}")

#%%
#Ejercicio 3.5: funcion leer_camion(nombre_archivo)
#El error que encontré es que cada vez que se ejecuta el for, los datos se van pisando 
# y a la vez se van agregando como diccionario a la lista, entonces, la última fila del archivo
# que corresponde a las Naranjas, pisa la fila anterior que a la vez pisó a la otra fila. En consecuencia,
# queda una lista formada por la última fila. Esto pasa ya que al asignar un valor a una determinada clave del diccionario,
# se asigna a todas las que tienen esa clave.

#La solución que encontré es definir el diccionario 'registro' y guardar cada fila en cada iteración allí y luego eso
# guardarlo en la lista.
#Código:
import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
    registro={}
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro = {encabezado[0] : fila[0], encabezado[1] : int(fila[1]), encabezado[2] : float(fila[2])}
            camion.append(registro)
    return camion

camion = leer_camion('C:/Python/ejercicios_python/Data/camion.csv')
pprint(camion)
