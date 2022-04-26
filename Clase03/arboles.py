# -*- coding: utf-8 -*-
"""
Created on Sun Mar 28 11:53:59 2021

@author: Valentin Colella
"""
import csv

from collections import Counter

def leer_parque(nombre_archivo, parque):
    f = open(nombre_archivo,encoding='utf-8')
    datosarchivo = csv.reader(f)
    encabezados = next(datosarchivo)
    lista = []
    for fila in datosarchivo:
       if fila[10] == parque:
           record = dict(zip(encabezados, fila))
           lista.append(record)
    f.close()
    return lista
       
        
def leer_especies(lista):
    especies = []
    for fila in lista :
        especies.append(fila['nombre_com'])
    especies = set(especies)
    return especies

def contar_ejemplares(lista):
    especies = []
    for fila in lista:
        especies.append(fila['nombre_com'])
    especies = Counter(especies)
    print('Cinco especies mas frecuentes: ')
    print(especies.most_common(5))
    return especies
    
def obtener_alturas(lista_arboles, especie):
    alturas = []
    for fila in lista_arboles:
        if fila['nombre_com'] == especie:
            alturas.append(float(fila['altura_tot']))
    return alturas
            
def calcular_alturas(alturas):
    suma = 0
    alturamaxima = max(alturas)
    print('Altura máxima de los Jacarandá en este parque:',alturamaxima)
    for i in alturas:
        suma += i
    alturapromedio = suma/len(alturas)
    print(f'Altura promedio de los Jacarandá en este parque: {alturapromedio:0.2f}')
    
def obtener_inclinaciones(lista_arboles, especie):
    inclinaciones = []
    for fila in lista_arboles:
        if fila['nombre_com'] == especie:
            inclinaciones.append(float(fila['inclinacio']))
    return inclinaciones    

def especimen_mas_inclinado(lista_arboles):
    b = {}
    especies = leer_especies(lista_arboles)
    for i in especies:
        inclinaciones = obtener_inclinaciones(lista_arboles, i)
        mas_inclinado = max(inclinaciones)
        b[i] = mas_inclinado
    max_key = max(b, key = b.get)
    b = {max_key:b[max_key]}
    return b
    
def especie_promedio_mas_inclinada(lista_arboles):
    especies = leer_especies(lista_arboles)
    suma = 0
    b = {}
    for i in especies:
        inclinaciones = obtener_inclinaciones(lista_arboles, i)
        for a in inclinaciones:
            suma += a
        inclinacionpromedio = suma / len(inclinaciones)
        b[i] = inclinacionpromedio
        inclinacionpromedio = 0
        suma = 0
    max_key = max(b, key = b.get)
    b = {max_key:b[max_key]}
    return b
    
    
for i in ('GENERAL PAZ', 'ANDES, LOS', 'CENTENARIO'):
    print(i)
    lista = leer_parque('../Data/arbolado-en-espacios-verdes.csv', i)
    especies = leer_especies(lista)
    cantidad_ejemplares = contar_ejemplares(lista)
    alturas = obtener_alturas(lista, 'Jacarandá')
    calcular_alturas(alturas)
    obtener_inclinaciones(lista, 'Falso Guayabo (Guayaba del Brasil)')
    mas_inclinado = especimen_mas_inclinado(lista)
    print(f'Especie con arbol más inclinado y su respectiva inclinación: {mas_inclinado}')
    promedio_inclinacion = especie_promedio_mas_inclinada(lista)
    print(f'Especie que en promedio tiene la mayor inclinación, y su respectivo promedio: {promedio_inclinacion}')
    print('\n')
    

''' Al correr el programa:
GENERAL PAZ
Cinco especies mas frecuentes: 
[('Casuarina', 97), ('Tipa blanca', 54), ('Eucalipto', 49), ('Palo borracho rosado', 44), ('Fenix', 40)]
Altura máxima de los Jacarandá en este parque: 16.0
Altura promedio de los Jacarandá en este parque: 10.20
Especie con arbol más inclinado y su respectiva inclinación: {'Macrocarpa (Ciprés de Monterrey o Ciprés de Lambert)': 70.0}
Especie que en promedio tiene la mayor inclinación, y su respectivo promedio: {'No Determinable': 25.0}


ANDES, LOS
Cinco especies mas frecuentes: 
[('Jacarandá', 117), ('Tipa blanca', 28), ('Ciprés', 21), ('Palo borracho rosado', 18), ('Lapacho', 12)]
Altura máxima de los Jacarandá en este parque: 25.0
Altura promedio de los Jacarandá en este parque: 10.54
Especie con arbol más inclinado y su respectiva inclinación: {'Jacarandá': 30.0}
Especie que en promedio tiene la mayor inclinación, y su respectivo promedio: {'Álamo plateado': 25.0}


CENTENARIO
Cinco especies mas frecuentes: 
[('Plátano', 137), ('Jacarandá', 45), ('Tipa blanca', 42), ('Palo borracho rosado', 41), ('Fresno americano', 38)]
Altura máxima de los Jacarandá en este parque: 18.0
Altura promedio de los Jacarandá en este parque: 8.96
Especie con arbol más inclinado y su respectiva inclinación: {'Falso Guayabo (Guayaba del Brasil)': 80.0}
Especie que en promedio tiene la mayor inclinación, y su respectivo promedio: {'Rosa de Siria': 25.0

'''
    
    



    
    
    
