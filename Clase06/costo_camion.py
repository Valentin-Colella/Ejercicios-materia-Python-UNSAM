from informe_funciones import leer_camion

'''Al importar informe_funciones, se ejecuta el script'''

def costoo_camion(nombre_archivo):
    costo = 0
    
    camion = leer_camion(nombre_archivo)
    for a,s in enumerate(camion):
        try:
            costo += s['cajones']*s['precio']
        except ValueError:
            print(f'Error detectado en fila {a}: {s}')
    return costo
   

costo = costoo_camion('../Data/camion.csv')
print('Costo total:', costo)

            
