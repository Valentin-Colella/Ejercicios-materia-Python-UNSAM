# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 19:18:37 2021

@author: HP
"""

import csv

def leer_camion(nombre_archivo):
    f = open(nombre_archivo)
    p = []
    filas = csv.reader(f)
    encabezados = next(filas)
    for fila in filas:
        record = dict(zip(encabezados, fila))
        p.append(record)
    f.close()     
    return p

def leer_precios(nombre_archivo):
    d = {}
    f = open(nombre_archivo)
    rows = csv.reader(f)
    for row in rows:
        try:
            d[row[0]] = float(row[1])
        except IndexError:
            print(' ')
    f.close()         
    return d

def costo_camion(camion):
    costo = 0
    for a,s in enumerate(camion, start=1):
        try:
            ncajones = int(s['cajones'])
            precio = float(s['precio'])
            costo += ncajones*precio
        except ValueError:
            print(f'Error detectado en fila {a}: {s}')
    return costo



camion = leer_camion('../Data/fecha_camion.csv')

costo = costo_camion(camion)

a = leer_precios('../Data/precios.csv')

ventas = 0
venta = 0
costos = 0
'''Otra forma de calcular las ventas, el costo y la ganancia:'''
for tipo in camion:
        costos = costos + ( int(tipo['cajones']) * float(tipo['precio']) )
        ventas = ventas + ( int(tipo['cajones']) * float(a[tipo['nombre']]) )
print(f'{ventas - costos}')

for s in camion:
    for b in a:
        if s['nombre'] == b:
            venta = venta + int(s['cajones'])*float(a[b])

ganancia = venta - costo

print(f'Costo: {costo}   Venta: {venta}   Ganancia: {ganancia:0.2f}') #Al ejecutar: Costo: 47671.15   Venta: 62986.1   Ganancia: 15314.95
        
   



