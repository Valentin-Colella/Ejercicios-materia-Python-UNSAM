# -*- coding: utf-8 -*-
"""
Created on Fri May 21 19:50:37 2021

@author: HP
"""

import fileparse
from lote import Lote
import formato_tabla
from camion_pares1 import Camion


def leer_camion(nombre_archivo_camion):
    '''Lee un archivo con el contenido de un camión
    y lo devuelve como un objeto Camion.'''
    with open(nombre_archivo_camion) as file:
        camiondicts = fileparse.parse_csv(file,
                                        select=['nombre','cajones','precio'],
                                        types=[str,int,float])
    camion = [Lote(d['nombre'], d['cajones'], d['precio']) for d in camiondicts]
    return Camion(camion)
    
    

def leer_precios(nombre_archivo_precios):
    with open(nombre_archivo_precios) as f:
        precios=fileparse.parse_csv(f,types=[str,float],has_headers=False)
    return precios

def datos_informe(camion,precios):
    '''Devuelve una lista de tuplas. Cada tupla es (nombre,cajones,precio,cambio)'''
    tabla = []
    for s in camion:
        for b in precios:
            if s.nombre == b[0]:
                cambio = b[1] - (s.precio)
                tupla =(s.nombre,s.cajones,s.precio,cambio)
                tabla.append(tupla) 
    return tabla


def imprimir_informe(data_informe,formateador):  
    
    #Muestro por pantalla los encabezados con el formato que se pidió
    formateador.encabezado(['Nombre', 'Cantidad', 'Precio', 'Cambio'])
    #Recorro la lista de tuplas y las voy mostrando por pantalla según formato
    for nombre, cajones, precio, cambio in data_informe:
        rowdata = [ nombre, str(cajones), f'{precio:0.2f}', f'{cambio:0.2f}' ]
        formateador.fila(rowdata)

                
def informe_camion(nombre_archivo_camion, nombre_archivo_precios, fmt=None):
    camion = leer_camion(nombre_archivo_camion)

    precios = leer_precios(nombre_archivo_precios)
    
    if fmt == None:
        fmt = 'txt'
    
    #Creo un objeto de la clase FormatoTablaFMT (FMT puede ser HTML, CSV o TXT)
    formateador = formato_tabla.crear_formateador(fmt) 
    
    data_informe=datos_informe(camion,precios)
    
    imprimir_informe(data_informe,formateador)
    
    
def main(parametros):
    if len(parametros) < 3:
        print(f'Uso adecuado: {sys.argv[0]} archivo_camion archivo_precios')
        print('Si quiere puede especificar el formato:')
        print(f'{sys.argv[0]} archivo_camion archivo_precios formato')
        raise SystemExit
                         
    camion = parametros[1]
    precios = parametros[2]
    if len(parametros)==4:
        fmt = parametros[3]
        informe_camion(camion,precios,fmt)
    else: 
        informe_camion(camion,precios)
    


if __name__ == '__main__':
    import sys
    main(sys.argv)