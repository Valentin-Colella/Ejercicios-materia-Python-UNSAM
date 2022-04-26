# -*- coding: utf-8 -*-
"""
Created on Tue May 18 14:47:50 2021

@author: HP
"""

from punto import Punto

class Rectangulo:
    def __init__(self,p_1,p_2):
        self.p_1 = p_1
        self.p_2 = p_2
        p_3 = Punto(p_1.x, p_2.y)
        p_4 = Punto(p_2.x, p_1.y)
        self.p_3 = p_3
        self.p_4 = p_4
        
    def base(self):
        base_ = max(self.p_1.x,self.p_2.x)
        return base_
        
    def altura(self):
        altura_ = max(self.p_1.y,self.p_2.y)
        return altura_
        
        
    def area(self):
        area_ = self.base() * self.altura()
        return area_
    
    def desplazar(desplazamiento):
        
    def rotar():
        
        
    
ul = Punto(0,2)
lr = Punto(1,0)
ll = Punto(0,0)
ur = Punto(1,2)
rect1 = Rectangulo(ul,lr)
rect2 = Rectangulo(ll,ur)
print(rect1.base())
print(rect2.altura())