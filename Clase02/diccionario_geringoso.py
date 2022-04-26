palabras = []
d = {}
try:
    a = int(input('Ingrese la cantidad de palabras (numero) que quiere traducir al geringoso: '))
    
except ValueError:
    print('No ingresó un número, vuelva a ejecutar el programa.')

for i in range(a):
    palabras.append(input("Ingrese la palabra: ")) ##palabras que piden ingresar: banana, manzana, mandarina


for i in palabras:
    palabra = i
    b = ''
    for c in palabra:
        if c == 'a' or c == 'e' or c == 'i' or c == 'o' or c == 'u':
            b = b + c + 'p' + c
        else:
            b = b + c
    d[palabra] = b
print('\n Diccionario: \n')
print(d) #Lo que obtuve: {'banana': 'bapanapanapa', 'manzana': 'mapanzapanapa', 'mandarina': 'mapandaparipinapa'}
