# -*- coding: utf-8 -*-
"""
Created on Fri May 21 19:55:52 2021

@author: Valentin Colella
"""

import csv

def parse_csv(lista, select = None, types = None,has_headers=True,silence_errors = True):
    '''
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
    
    '''

    if select and not has_headers:
        raise RuntimeError("Para seleccionar, necesito encabezados.")
            
    filas = csv.reader(lista)
    if has_headers:        #Si el archivo tiene encabezados realiza todo lo siguiente:
        # Lee los encabezados del archivo
        encabezados = next(filas)
        
            # Si se indicó un selector de columnas,
            # buscar los índices (posiciones) de las columnas especificadas. (esto hace encabezados.index(nombre_columna) )
            # Y en ese caso achicar el conjunto de encabezados para diccionarios

        if select:
            indices = [encabezados.index(nombre_columna) for nombre_columna in select]
            encabezados = select
        else:
            indices = []

        registros = []
        for i,fila in enumerate(filas):
            if not fila:    # Saltear filas vacías
                continue
                # Filtrar la fila si se especificaron columnas
            if indices:
                fila = [fila[index] for index in indices] #De todo lo que tengo en la fila 
                                                              #me lee sólo los que están en la misma
                                                              #columna que lo que envié en select.
        
                                                             
            if types:
                try:
                    fila = [func(val) for func, val in zip(types, fila)]
                except ValueError as e:
                    if silence_errors:
                        print(f'Fila {i+1}: No pude convertir {fila}')
                        print(f'Fila {i+1}: Motivo: {e}')
                
                # Armar el diccionario
            registro = dict(zip(encabezados, fila))
            registros.append(registro)
    else:   #Si el archivo no tiene encabezados:
        registros = []
        for i,fila in enumerate(filas):
            if not fila:    # Saltear filas vacías
                continue
            if types:
                try:
                    fila = [func(val) for func, val in zip(types, fila)]
                except ValueError as e:
                    if silence_errors:
                        print(f'Fila {i+1}: No pude convertir {fila}')
                        print(f'Fila {i+1}: Motivo: {e}')
                        if i==0:
                            print('Cuidado. Hay encabezados.')
            registros.append(tuple(fila))
            

    return registros

def leer_archivo(file_name):
    with open(file_name) as file:
        data = parse_csv(file,select=['nombre','cajones','precio'],types=[str,int,float])
        
    return data


#data_ = leer_archivo('nombre_archivo')


