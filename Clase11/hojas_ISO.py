# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 18:50:40 2021

@author: HP
"""

def hojas_iso(N):
    if N == 0:
        largo = 1189
        ancho = 841
        return ancho, largo
    else:
        ancho,largo = hojas_iso(N-1)
        ancho_1 = largo//2
        largo_1 = ancho
        
        return ancho_1, largo_1
    
    
#a = hojas_iso(6)
#print(a)
        