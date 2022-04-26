# -*- coding: utf-8 -*-
"""
Created on Sun May 23 17:31:08 2021

@author: HP
"""

from vigilante import vigilar
import csv
import informe
import formato_tabla

def parsear_datos(lines):
    rows = csv.reader(lines)
    #equivalente a la función elegir_columnas
    rows_ = ([row[index] for index in [0,1,2]] for row in rows)      
    #equivalente a la funcion cambiar_tipo                                         
    rows_ = ([func(val) for func, val in zip([str,float,int], row)] for row in rows_)
    #equivalente a la funcion hace_dicts
    rows_ = (dict(zip(['nombre','precio','volumen'], row)) for row in rows_)
    return rows_

def ticker(camion_file, log_file, fmt):
    camion = informe.leer_camion(camion_file)
    filas = parsear_datos(vigilar(log_file))
    #equivalente a la función filtrar_datos
    filas = (fila for fila in filas if fila['nombre'] in camion) 
    formateador = formato_tabla.crear_formateador(fmt)
    formateador.encabezado(['Nombre', 'Precio', 'Volumen'])
    for fila in filas:
        rowdata = [ fila['nombre'], str(fila['precio']), str(fila['volumen']) ]
        formateador.fila(rowdata)

#ticker('../Data/camion.csv', '../Data/mercadolog.csv', 'html')

   