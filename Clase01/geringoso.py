# -*- coding: utf-8 -*-
a = input('Ingrese la palabra de la cual quiere saber su geringoso (todo en minúsculas): ')
b = ' '
for c in a:
    if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
      b = b + c + 'p' + c
    else:
        b = b + c
print(b)
