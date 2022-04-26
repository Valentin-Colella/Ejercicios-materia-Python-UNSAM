# -*- coding: utf-8 -*-
"""
Created on Mon May 10 14:44:09 2021

@author: HP
"""
import os
from datetime import datetime
import shutil

def fecha_nombre(nombre_archivo):
    #La fecha son los últimos 8 caracteres del nombre del archivo
    fecha = str(nombre_archivo[-8:len(nombre_archivo)]) 
    fecha=datetime.strptime(fecha,'%Y%m%d') #Convierto a datetime
    nombre_archivo = nombre_archivo[0:-8] ##El nuevo nombre es sin los ultimos 8 caracteres
    return nombre_archivo, fecha
    
    
def procesar_(root,nombre_viejo,extension):
    nombre_nuevo,fecha=fecha_nombre(nombre_viejo) ##Obtengo la fecha y el nombre nuevo
    ts_modifi = fecha.timestamp() #Convierto a timestamp
    os.rename(os.path.join(root,nombre_viejo+extension),
              os.path.join(root,nombre_nuevo+extension)) #renombro el archivo
    os.utime(os.path.join(root,nombre_nuevo+extension), #cambio la fecha de modificación
             ((datetime.now()).timestamp(),ts_modifi))
    shutil.move(os.path.join(root,nombre_nuevo+extension), #muevo el archivo
                os.path.join('..','Data','imgs_procesadas'))
    
    
def leer_archivos_png(directorio):
    lista_root = []
    archivos_carpeta=os.walk(directorio) 
    for root,dirs,files in archivos_carpeta:  
        for file in files:
            nombre_archivo,extension = os.path.splitext(file)  ##Me guardo la extensión y el nombre del archivo en cuestión
            ##Si el archivo es .png, lo guardo
            if extension == '.png':
                ##Paso como parámetros el directorio donde se encuentra la imagen
                #el nombre del archivo y la extensión
                procesar_(root,nombre_archivo,extension)
                lista_root.append(root)
    #Elimino las subcarpetas vacias, recorro la lista de roots en reversa para ir de 
    #'menor a mayor'
    for root in reversed(lista_root):   
        try:
            os.rmdir(root)
        except: 
            OSError
            
            
def main(parametros):
    if len(parametros) != 2:
        raise SystemExit(f'Uso adecuado: {sys.argv[0]} ' 'directorio_a_leer')
    directorio=parametros[1]
    leer_archivos_png(directorio)
    

if __name__ == '__main__':
    import sys
    main(sys.argv)              