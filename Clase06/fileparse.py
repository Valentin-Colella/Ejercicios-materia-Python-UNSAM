# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 14:38:43 2021

@author: HP
"""

import csv



def parse_csv(nombre_archivo, select = None, types = None,has_headers=True):
    '''
    Parsea un archivo CSV en una lista de registros.
    Se puede seleccionar sólo un subconjunto de las columnas, determinando el parámetro select, que debe ser una lista de nombres de las columnas a considerar.
    '''
    with open(nombre_archivo) as f:
        
            
        filas = csv.reader(f)
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
            for fila in filas:
                if not fila:    # Saltear filas vacías
                    continue
                # Filtrar la fila si se especificaron columnas
                if indices:
                    fila = [fila[index] for index in indices] #De todo lo que tengo en la fila 
                                                              #me lee sólo los que están en la misma
                                                              #columna que lo que envié en select.
        
                                                             
                if types:
                    fila = [func(val) for func, val in zip(types, fila) ]
                
                # Armar el diccionario
                registro = dict(zip(encabezados, fila))
                registros.append(registro)
        else:   #Si el archivo no tiene encabezados:
            registros = []
            for fila in filas:
                if not fila:    # Saltear filas vacías
                    continue
                if types:
                    fila = [func(val) for func, val in zip(types, fila)]
                registros.append(tuple(fila))
            

    return registros



