# -*- coding: utf-8 -*-
"""
Created on Tue May 18 17:12:49 2021

@author: HP
"""

class Cola:
    '''Representa a una cola, con operaciones de encolar y desencolar.
    El primero en ser encolado es tambien el primero en ser desencolado.
    '''

    def __init__(self):
        '''Crea una cola vacia.'''
        self.items = []

    def encolar(self, x):
        '''Encola el elemento x.'''
        self.items.append(x)

    def desencolar(self):
        '''Elimina el primer elemento de la cola 
        y devuelve su valor. 
        Si la cola esta vacia, levanta ValueError.'''
        if self.esta_vacia():
            raise ValueError('La cola esta vacia')
        return self.items.pop(0)

    def esta_vacia(self):
        '''Devuelve 
        True si la cola esta vacia, 
        False si no.'''
        return len(self.items) == 0
    
class TorreDeControl():
    
    def __init__(self):
        '''Defino dos objetos de tipo Cola
        para identificar arribos y salidas'''
        self.arribos = Cola()
        self.salidas = Cola()
    
    def nuevo_arribo(self,avion):
        ''' Encolo en la lista arribos'''
        self.arribos.encolar(avion)

    def nueva_partida(self,avion):
        '''Encolo en la lista salidas'''
        self.salidas.encolar(avion)
        
    def ver_estado(self):
        '''Si ambas listas están vacías lo muestra por pantalla.
        Sino, muestra cuales vuelos están esperando para aterrizar y cuales para 
        despegar'''
        if self.arribos.esta_vacia() and self.salidas.esta_vacia():
            print('No hay vuelos en espera')
        else:
            print('Vuelos esperando para aterrizar:',end=' ')
            for vuelos in self.arribos.items:
                print(f'{vuelos}',end=' ')
            print('\nVuelos esperando para despegar:',end=' ')
            for vuelos in self.salidas.items:
                print(f'{vuelos}',end=' ')
    
    def asignar_pista(self):
        '''Si las listas están vacías lo muestra por pantalla
        Sino, primero desencola los arribos (hasta que esta lista esté vacía)
        y luego los despegues. Siempre y cuando las listas NO estén vacías.'''
        if self.arribos.esta_vacia() and self.salidas.esta_vacia():
            print('No hay vuelos en espera')
        
        elif not self.arribos.esta_vacia(): 
            print(f'\nEl vuelo {self.arribos.desencolar()} aterrizó con éxito')
            
        elif not self.salidas.esta_vacia():
            print(f'El vuelo {self.salidas.desencolar()} despegó con éxito' )
            
        
 
torre = TorreDeControl()
torre.nuevo_arribo('AR156')
torre.nueva_partida('KLM1267')
torre.nuevo_arribo('AR32')
torre.ver_estado()
torre.asignar_pista()
torre.asignar_pista()
torre.asignar_pista()
torre.asignar_pista()



