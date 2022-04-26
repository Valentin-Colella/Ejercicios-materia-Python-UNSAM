import csv

def leer_camion(nombre_archivo):
    camion = []
    f = open(nombre_archivo)
    rows = csv.reader(f)
    headers = next(rows)
    for row in rows:
        d = {headers[0] : row[0], headers[1] : int(row[1]), headers[2] : float(row[2])}
        camion.append(d)
        
            
    f.close()
    return camion

def leer_precios(nombre_archivo):
    d = {}
    f = open(nombre_archivo)
    rows = csv.reader(f)
    for row in rows:
        try:
            d[row[0]] = float(row[1])
        except IndexError:
            print(' ')
    f.close()         
    return d


camion = leer_camion('../Data/camion.csv')
costo = 0
venta = 0
for s in camion:
    costo = costo + s['cajones']*s['precio']
a = leer_precios('../Data/precios.csv')

for s in camion:
    for b in a:
        if s['nombre'] == b:
            venta = venta + s['cajones']*a[b]

ganancia = venta - costo

print(f'Costo: {costo}   Venta: {venta}   Ganancia: {ganancia}') #Al ejecutar: Costo: 47671.15   Venta: 62986.1   Ganancia: 15314.949999999997
        
   



