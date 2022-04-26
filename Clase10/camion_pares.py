# -*- coding: utf-8 -*-
"""
Created on Mon May 31 16:52:15 2021

@author: HP
"""

class Camion:
    def __init__(self,lotes):
        self.lotes=lotes
        
    def precio_total(self):
        return sum(l.costo() for l in self.lotes)
    
    def __iter__(self):
        return self.lotes.__iter__()

    def __len__(self):
        return len(self.lotes)
    
    def __getitem__(self,index):
        return self.lotes[index]
    
    def __delitem__(self,a):
        del self.lote[a]
    
    def __contains__(self,nombre):
        return any([lote.nombre==nombre for lote in self.lotes])
        
    def contar_cajones(self):
        from collections import Counter
        cantidad_total=Counter()
        for l in self.lotes:
            cantidad_total[l.nombre] += l.cajones
        return cantidad_total
    
    
    


