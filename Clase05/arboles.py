# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 16:50:21 2021

@author: HP
"""
import csv
import matplotlib.pyplot as plt
import numpy as np

def leer_arboles(nombre_archivo):
    f = open(nombre_archivo,encoding='utf-8')
    datosarchivo = csv.reader(f)
    encabezados = next(datosarchivo)
    lista = [dict(zip(encabezados,s)) for s in datosarchivo ]
    f.close()
    return lista

def medidas_de_especies(especies,arboleda):
    dict={especie:([(float(arbol['altura_tot']),float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com'] == especie])for especie in especies}
    return dict

def graficar_Jacarandá(HyD):
    altos = [i[0] for i in HyD]
    plt.title('Histograma, altura Jacarandás')
    plt.hist(altos,bins=17)
    
def graficar_especies(dic):  
    for i in dic:
        plt.figure()
        a=np.array(dic[i]).copy()  #Vector con las alturas y los diametros
        h=a[0:len(a),0]       ##Vector con las alturas
        d=a[0:len(a),1]       ##Vector con los diametros
        N=len(a)
        plt.xlim(0,260)
        plt.ylim(0,50)
        plt.xlabel("diametro (cm)")
        plt.ylabel("alto (m)")
        plt.title(f'Relación diámetro-alto para {i}')
        plt.scatter(d,h,alpha=0.2,s=20*(d/h), c=(np.random.rand(N)))
        

nombre_archivo=('../Data/arbolado-en-espacios-verdes.csv')
especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
arboleda = []
arboleda = leer_arboles(nombre_archivo)
HyD=[(float(arbol['altura_tot']),float(arbol['diametro'])) for arbol in arboleda if arbol['nombre_com']=='Jacarandá']
dic = {}
dic=medidas_de_especies(especies,arboleda)

graficar_Jacarandá(HyD)
graficar_especies(dic)        #LOS GRAFICOS SE ABREN EN OTRA VENTANA
   
