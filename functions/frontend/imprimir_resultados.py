from tabulate import tabulate


def imprimir_tabulate(ruta):
    # Crear una tabla con las líneas de metro
    tabla = [[i+1, linea] for i, linea in enumerate(ruta)]
    print(tabulate(tabla, headers=["Paso", "Línea de Metro"]))


def imprimir_ruta_menos_transbordos(origen , destino, camino, transbordos, estaciones_transbordo, tiempo_recorrido, hora_llegada ):

    if camino:
        print(f"La ruta con menor cantidad de transbordos entre {origen} y {destino} es:")
        print( "Tiempo estimado de viaje[Hrs:Min:Seg]: ",tiempo_recorrido)
        print("Hora de llegada: ", hora_llegada.time())
        imprimir_tabulate(camino)
        #print(" -> ".join(camino))
        print(f"Número total de transbordos realizados: {transbordos}")
        if estaciones_transbordo:
            print(f"Transbordos realizados en las siguientes estaciones: {', '.join(estaciones_transbordo)}")
        else:
            print("No se realizaron transbordos.")
    else:
        print("No se encontró una ruta.")


def imprimir_ruta_corta(ruta, hora_llegada, tiempo_recorrido, origen, destino):
    
    print( "Partida:  ", origen)
    print( "Destino:  ", destino)
    print( "Tiempo estimado de viaje[Hrs:Min:Seg]: ",tiempo_recorrido)
    print("Hora de llegada: ", hora_llegada.time())


    #print("ruta de viaje: ", ruta)
    imprimir_tabulate(ruta)