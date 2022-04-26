# -*- coding: utf-8 -*-
"""
Created on Mon May 17 12:51:13 2021

@author: HP
"""

def crear_formateador(nombre):
    if nombre == 'txt':
        formateador_ = FormatoTablaTXT()
    elif nombre == 'csv':
        formateador_ = FormatoTablaCSV()
    elif nombre == 'html':
        formateador_ = FormatoTablaHTML()

    return formateador_

def imprimir_tabla(archivo,encabezados,formateador):
    #Imprimo el encabezado, el formateador sirve para identificar cual formato es.
    formateador.encabezado(encabezados) 
    #Cada fila del archivo es un objeto de la clase lote.
    for c in archivo:
        lista=[]
        for colname in encabezados:
            lista.append(str(getattr(c, colname)))
        formateador.fila(lista)
        
        
class FormatoTabla:
    def encabezado(self, headers):
        '''
        Crea el encabezado de la tabla.
        '''
        raise NotImplementedError()

    def fila(self, data_fila):
        '''
        Crea una única fila de datos de la tabla.
        '''
        raise NotImplementedError()
        
        
class FormatoTablaTXT(FormatoTabla):
    '''
    Generar una tabla en formato TXT
    '''
    def encabezado(self, headers):
        for h in headers:
            print(f'{h:>10s}', end=' ')
        print()
        print(('-'*10 + ' ')*len(headers))

    def fila(self, data_fila):
        for d in data_fila:
            print(f'{d:>10s}', end=' ')
        print()
        
        
class FormatoTablaCSV(FormatoTabla):
    '''
    Generar una tabla en formato CSV
    '''
    def encabezado(self, headers):
        print(','.join(headers))

    def fila(self, data_fila):
        print(','.join(data_fila))
        
        
class FormatoTablaHTML(FormatoTabla):
    '''
    Generar una tabla en formato HTML
    '''
     
    def encabezado(self,headers):
        print('<tr><th>'+'</th><th>'.join(headers)+'</th></tr>')
        
    def fila(self, data_fila):
        print('<tr><td>'+'</td><td>'.join(data_fila)+'</td></tr>')
                
        
        
        
        
        
        
        
        
        