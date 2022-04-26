
import csv
def costo_camion(nombre_archivo):
    costo = 0
    f = open(nombre_archivo)
    rows = csv.reader(f)
    next(rows)
    for row in rows:
        try:
            costo = costo + int(row[-2])*float(row[-1])
        except ValueError:
            print('Error detectado. Revisar archivo')
    f.close()       
    return costo

costo = costo_camion('../Data/camion.csv')
print('Costo total:', costo)
            
