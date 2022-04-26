# -*- coding: utf-8 -*-
"""
Created on Tue May 11 17:39:59 2021

@author: HP
"""

import os
import pandas as pd

def parques_(df_parques,nombre_parque):
    cols = ['altura_tot', 'diametro']
    df_tipas_parquess = df_parques[df_parques['nombre_cie'] == nombre_parque][cols].copy()
    #Cambio el nombre de las columnas.
    df_tipas_parquess = df_tipas_parquess.rename(columns={'altura_tot':'altura_arbol',
                                                'diametro':'diametro_altura_pecho'})
    df_tipas_parquess=df_tipas_parquess.assign(ambiente='parque')
    return df_tipas_parquess
    
    
def veredas_(df_veredas,nombre_vereda):
    cols = ['altura_arbol', 'diametro_altura_pecho']
    #Armo un nuevo dataframe con los datos altura_arbol y diametro_altura_pecho
    #del arbol que quiero (nombrado en nombre_vereda). Las columnas son altura_arbol y diametro_altura_pecho
    df_tipas_veredass = df_veredas[df_veredas['nombre_cientifico'] == nombre_vereda][cols].copy()
    #Agrego una columna llamada ambiente y en todas las filas debajo de éste titulo
    #la palabra vereda.
    df_tipas_veredass=df_tipas_veredass.assign(ambiente='vereda')
    return df_tipas_veredass

def parques_veredas(nombre_vereda,nombre_parque,df_veredas,df_parques):
    '''Recibe como parámetros los nombres científicos de los árboles y los dataframe
    correspondientes.
    El primer nombre científico tiene que ser el relacionado a veredas y el
    segundo a parques.
    El primer dataframe relacionado a veredas y el segundo a parques.'''
    df_tipas_veredas=veredas_(df_veredas,nombre_vereda)
    df_tipas_parques=parques_(df_parques,nombre_parque)
    df_tipas = pd.concat([df_tipas_veredas, df_tipas_parques])
    df_tipas.boxplot('diametro_altura_pecho',by = 'ambiente')
    df_tipas.boxplot('altura_arbol',by = 'ambiente')

directorio = '../Data'
archivo =  'arbolado-publico-lineal-2017-2018.csv'
archivo1 = 'arbolado-en-espacios-verdes.csv'
fname = os.path.join(directorio,archivo)
fname1 = os.path.join(directorio,archivo1)
df_veredas = pd.read_csv(fname)
df_parques = pd.read_csv(fname1)

parques_veredas('Jacarandá mimosifolia','Jacarandá mimosifolia', df_veredas, df_parques) 
#Si quiero hacerlo para otras especies simplemente le paso otros nombres,
#siempre respetando el orden de los parámetros especificados dentro de la función.

