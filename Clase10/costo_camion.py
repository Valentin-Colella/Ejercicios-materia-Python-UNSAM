# -*- coding: utf-8 -*-
"""
Created on Sat May 22 17:16:52 2021

@author: HP
"""

from informe import leer_camion


'''Al importar informe_funciones, se ejecuta el script'''

def costo_camion(nombre_archivo):
    costo = 0
    
    camion = leer_camion(nombre_archivo)
    costo = camion.precio_total()
    return costo
   
def main(parametros):
    if len(parametros) != 2:
        raise SystemExit(f'Uso adecuado: {sys.argv[0]} ' 'archivo_camion')
    camion=parametros[1]
    costo = costo_camion(camion)
    print('Costo total:', costo)

if __name__ == '__main__':
    import sys
    main(sys.argv)