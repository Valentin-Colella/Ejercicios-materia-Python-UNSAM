# -*- coding: utf-8 -*-
"""
Created on Fri May 21 19:59:29 2021

@author: HP
"""
from lote import Lote

class Camion:

    def __init__(self, lotes):
        self.lotes = lotes

    def __iter__(self): #Hago iterable el objeto
        return self.lotes.__iter__()
    
    def __len__(self): #Para poder definir la longitud del objeto
        return len(self.lotes)

    def __getitem__(self, index):  #permite usar operador [] (indexador)
        return self.lotes[index]

    def __contains__(self, nombre): #Para poder usar 'in' o 'not in'
        return any(lote.nombre == nombre for lote in self.lotes)
    
    def __delitem__(self, posicion): #Elimina un lote de 'camion'. 
                                     #Por ejemplo si quiero eliminar la posicion
                                     #0: del camion[0] 
        del self.lotes[posicion]
        
    def __setitem__(self, posicion ,nuevo): #Cambio un lote de 'camion'. 
                                            #Para usarlo, por ej: camion[1]=['Kiwi', 15, 100.2]
        nuevo=Lote(str(nuevo[0]),int(nuevo[1]),float(nuevo[2]))
        self.lotes[posicion] = nuevo
        
    def append(self,nuevo): #Para agregar un nuevo lote al final
        nuevo=Lote(str(nuevo[0]),int(nuevo[1]),float(nuevo[2]))
        self.lotes.append(nuevo)
        
    def precio_total(self):
        return sum(l.costo() for l in self.lotes)

    def contar_cajones(self):
        from collections import Counter
        cantidad_total = Counter()
        for lote in self.lotes:
            cantidad_total[lote.nombre] += lote.cajones
        return cantidad_total
    
        
