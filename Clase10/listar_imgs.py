# -*- coding: utf-8 -*-
"""
Created on Mon May 24 16:04:29 2021

@author: HP
"""

import os 

def imprimir_archivos_png(directorio):
    archivos_carpeta=os.walk(directorio) 
    archivos_png=(((root,file) for file in files if os.path.splitext(file)[1]=='.png') for root,dirs,files in archivos_carpeta )
    #Dos for ya que son dos generadores
    for pares in archivos_png:
        for imagenes in pares:
            print(imagenes)
            
            
def main(parametros):
    if len(parametros) != 2:
        raise SystemExit(f'Uso adecuado: {sys.argv[0]} ' 'directorio_a_leer')
    directorio=parametros[1]
    imprimir_archivos_png(directorio)
    

    
if __name__ == '__main__':
    import sys
    main(sys.argv)