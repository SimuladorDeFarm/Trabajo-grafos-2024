import csv

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

