# -*- coding: utf-8 -*-
"""
Created on Mon May 10 12:24:56 2021

@author: HP
"""

import os 

def imprimir_archivos_png(directorio):
    archivos_png = []
    archivos_carpeta=os.walk(directorio) 
    for root,dirs,files in archivos_carpeta:  
        for file in files:
            extension = os.path.splitext(file)[1]  ##Me guardo la extensión del archivo en cuestión
            ##Si el archivo es .png, lo guardo
            if extension == '.png': 
                archivos_png.append(file)
    print(f'Los archivos .png encontrados son:\n {archivos_png}')
    
def main(parametros):
    if len(parametros) != 2:
        raise SystemExit(f'Uso adecuado: {sys.argv[0]} ' 'directorio_a_leer')
    directorio=parametros[1]
    imprimir_archivos_png(directorio)
    

    
if __name__ == '__main__':
    import sys
    main(sys.argv)