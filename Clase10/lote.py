# -*- coding: utf-8 -*-
"""
Created on Fri May 21 19:56:24 2021

@author: HP
"""

class Lote:
    def __init__(self,nombre,cajones,precio):
        self.nombre=nombre
        self.cajones=cajones
        self.precio=precio
        
    def costo(self):
        costo = self.cajones * self.precio
        return costo
        
    def vender(self,cantidad):
        self.cajones -= cantidad
        
    def __repr__(self):
        return f'Lote({self.nombre}, {self.cajones}, {self.precio})'