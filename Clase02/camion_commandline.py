import csv
import sys

def costo_camion(nombre_archivo):
    costo = 0
    f = open(nombre_archivo)
    rows = csv.reader(f)
    next(rows)
    for row in rows:
        try:
            costo = costo + float(row[-2])*float(row[-1])
        except ValueError:
            print('Error detectado. Revisar archivo')
    f.close()        
    return costo

if len(sys.argv) == 2:
    nombre_archivo = sys.argv[1]
else:
    nombre_archivo = '../Data/camion.csv'
costo = costo_camion(nombre_archivo)
print('Costo total:', costo)
