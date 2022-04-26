def buscar_precio(fruta):
    n = 1
    with open('../Data/precios.csv', 'rt') as f:
        for line in f:
                row = line.split(',')
                if row[0] == fruta:
                    print('El precio de la', fruta,'es',row[1])
                    n = 0
        if n == 1:
            print(fruta,'no figura en el listado de precios')
    

fruta = input('Ingrese el nombre de la fruta o verdura: ')
buscar_precio(fruta)

