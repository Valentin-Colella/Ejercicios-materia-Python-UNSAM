# -*- coding: utf-8 -*-
"""
Created on Sat May 15 11:39:58 2021

@author: HP
"""

from informe import leer_camion

'''Al importar informe_funciones, se ejecuta el script'''

def costoo_camion(nombre_archivo):
    costo = 0
    
    camion = leer_camion(nombre_archivo)
    for a,s in enumerate(camion):
        try:
            costo += s.cajones*s.precio
        except ValueError:
            print(f'Error detectado en fila {a}: {s}')
    return costo
   
def main(parametros):
    if len(parametros) != 2:
        raise SystemExit(f'Uso adecuado: {sys.argv[0]} ' 'archivo_camion')
    camion=parametros[1]
    costo = costoo_camion(camion)
    print('Costo total:', costo)

if __name__ == '__main__':
    import sys
    main(sys.argv)