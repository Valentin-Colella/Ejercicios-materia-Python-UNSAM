# -*- coding: utf-8 -*-
"""
Created on Thu May  6 16:17:31 2021

@author: HP
"""

from datetime import datetime

a=input('Ingrese su fecha de nacimiento en formato dd/mm/AAAA: ')
date_object = datetime.strptime(a, '%d/%m/%Y')

hoy = datetime.now()

diferencia = hoy - date_object

total_segundos = diferencia.total_seconds()

print('Total de segundos vividos: ',total_segundos)




