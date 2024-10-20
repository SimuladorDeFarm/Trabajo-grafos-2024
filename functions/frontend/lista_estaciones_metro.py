import csv
import numpy as np

def lista_metro():

    # Lista para almacenar los datos del CSV
    data = []

    # Abrir y leer el archivo CSV
    with open('./functions/base_datos/metro_santiago.csv', mode='r') as file:
        reader = csv.reader(file)
        
        # Recorremos cada fila del archivo y la añadimos al array (lista)
        for row in reader:
            data.append(row)

    # Imprimir los datos en la lista
    return data

#idea desechada un array que contenga las etaciones y sus lineas
def estacion_linea():

    lista = lista_metro()
    # Crear un array de 200 filas y 2 columnas con valores inicializados en 0
    #array = [[0 for _ in range(200)] for _ in range(2)] 
    array = [[0, 0] for _ in range(200)]

    i = 0
    largo_lista = len(lista)
    while i <  largo_lista:

        array[i][0] = lista[i][0]

        i+=1
    i = 0
    while i < largo_lista:

        array[i][1] = lista[i][3]
        i+=1

    print(array)
    

    array_np = np.array(array)

    # Guardar el array como CSV en la misma carpeta
    np.savetxt('linas_estaciones.csv', array_np, delimiter=',', header='estaciones,lineas',    comments='', fmt='%s')