# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 17:24:40 2021

@author: HP
"""

import fileparse

def leer_camion(nombre_archivo_camion):
    camion=fileparse.parse_csv(nombre_archivo_camion, types = [str, int, float])
    return camion

def leer_precios(nombre_archivo_precios):
    precios=fileparse.parse_csv(nombre_archivo_precios,types=[str,float],has_headers=False)
    return precios

def costo_camion(camion):
    costo = 0
    for a,s in enumerate(camion, start=1):
        try:
            costo += s['cajones']*s['precio']
        except ValueError:
            print(f'Error detectado en fila {a}: {s}')
    return costo

def venta_(camion,a):
    venta = 0
    for s in camion:
        for b in a:
            if s['nombre'] == b[0]:
                venta = venta + (s['cajones'])*(b[1])
    return venta

def separacion(headers):
    guiones = '---------- ---------- ---------- ----------'
    headers = '%10s %10s %10s %10s' % headers
    print(headers)
    print(guiones)

def imprimir_informe(camion,precios):
    tabla = []
    for s in camion:
        for b in precios:
            if s['nombre'] == b[0]:
                cambio = b[1] - (s['precio'])
                tupla =(s['nombre'],s['cajones'],s['precio'],cambio)
                tabla.append(tupla)    
    headers = ('Nombre', 'Cajones', 'Precio', 'Cambio')
    separacion(headers)
                
    for r in tabla:
        peso = f'${r[2]}'
        print(f'{r[0]:>10s} {r[1]:10d} {peso:>10s} {r[3]:10.2f}')
    venta=venta_(camion,precios)
    
    costo=costo_camion(camion)
        
    ganancia = venta - costo

    print(f'\nCosto: {costo}   Venta: {venta}   Ganancia: {ganancia:>0.2f}') 
        

def informe_camion(nombre_archivo_camion, nombre_archivo_precios):
    camion = leer_camion(nombre_archivo_camion)
    

    precios = leer_precios(nombre_archivo_precios)
    
    
    imprimir_informe(camion,precios)


files = ['../Data/camion2.csv', '../Data/camion.csv']
for name in files:
        print(f'{name:-^43s}')
        informe_camion(name, '../Data/precios.csv')
        print()