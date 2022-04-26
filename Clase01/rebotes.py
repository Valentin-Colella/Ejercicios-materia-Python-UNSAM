# -*- coding: utf-8 -*-

rebotes = (1,2,3,4,5,6,7,8,9,10)
altura = 100
for i in rebotes:
    altura = altura * (3/5)
    altura = round(altura, 4) #redondea 4 dígitos, (en este caso porque use un 4)
    print(altura)
