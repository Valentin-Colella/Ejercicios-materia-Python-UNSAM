# -*- coding: utf-8 -*-
"""
Created on Tue May 18 16:09:30 2021

@author: HP
"""

class Canguro:
    def __init__(self,nombre):
        self.nombre = nombre
        self.contenido_marsupio = []
        
    def meter_en_marsupio(self,objeto):
        self.contenido_marsupio.append(objeto)
        
    def __str__(self):
        return f'{self.nombre} {self.contenido_marsupio}'
    
#%%    
class Canguro:
    """Un Canguro es un marsupial."""
    
    def __init__(self, nombre):
        """Inicializar los contenidos del marsupio.

        nombre: string
        contenido: contenido inicial del marsupio, lista.
        """
        self.nombre = nombre
        self.contenido_marsupio = []

    def __str__(self):
        """devuelve una representación como cadena de este Canguro.
        """
        t = [ self.nombre + ' tiene en su marsupio:' ]
        for obj in self.contenido_marsupio:
            s = '    ' + object.__str__(obj)
            t.append(s)
        return '\n'.join(t)

    def meter_en_marsupio(self, item):
        """Agrega un nuevo item al marsupio.

        item: objecto a ser agregado
        """
        self.contenido_marsupio.append(item)
        
    # El problema estaba en __init__(self,contenido=[]), ya que luego se igualaba
    # self.contenido_marsupio = contenido. Entonces, como contenido es un atributo
    # y luego se lo iguala a contenido_marsupio, se va a estar modificando contenido_marsupio
    # de cualquier objeto perteneciente a la clase Canguro.
       
#%%
