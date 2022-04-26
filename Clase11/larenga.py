# -*- coding: utf-8 -*-
"""
Created on Sat May 29 11:52:12 2021

@author: HP
"""

def triangulo(f,c):
    if f==c or c==0:
        return 1
    else:
        a = triangulo(f-1,c-1)+triangulo(f-1,c)
        return a
    
    
    
#print(triangulo(5,2))