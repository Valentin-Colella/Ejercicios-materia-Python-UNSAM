# -*- coding: utf-8 -*-

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

def hacer_informe(camion,precios):
    tabla = []
    for s in camion:
        for b in precios:
            if s['nombre'] == b:
                cambio = float(precios[b]) - float(s['precio'])
                tupla =(s['nombre'],int(s['cajones']),float(s['precio']),float(cambio))
                tabla.append(tupla)           
    return tabla

def venta_(camion,a):
    venta = 0
    for s in camion:
        for b in a:
            if s['nombre'] == b:
                venta = venta + int(s['cajones'])*float(a[b])
    return venta

def separacion(headers):
    guiones = '---------- ---------- ---------- ----------'
    headers = '%10s %10s %10s %10s' % headers
    print(headers)
    print(guiones)

    
camion = leer_camion('../Data/fecha_camion.csv')

costo = costo_camion(camion)

a = leer_precios('../Data/precios.csv')

informe = hacer_informe(camion,a)

headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')

separacion(headers)

for r in informe:
    peso = f'${r[2]}'
    print(f'{r[0]:>10s} {r[1]:10d} {peso:>10s} {r[3]:10.2f}')

venta = venta_(camion,a)

ganancia = venta - costo

print(f'\nCosto: {costo}   Venta: {venta}   Ganancia: {ganancia:>0.2f}') 

''' Lo que obtengo: 
    
    Nombre    Cajones     Precio     Cambio
---------- ---------- ---------- ----------
      Lima        100      $32.2       8.02
   Naranja         50      $91.1      15.18
     Caqui        150    $103.44       2.02
 Mandarina        200     $51.23      29.66
   Durazno         95     $40.37      33.11
 Mandarina         50      $65.1      15.79
   Naranja        100     $70.44      35.84

Costo: 47671.15   Venta: 62986.1   Ganancia: 15314.95

'''