# -*- coding: utf-8 -*-
"""
Created on Tue May 18 14:49:43 2021

@author: HP
"""

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

    # Used with `repr()`
    def __repr__(self):
        return f'Punto({self.x}, {self.y})'
    
    
    
a = Punto(1,2)
b = Punto(2,3)
a.y = 5
print(a)
print(b)