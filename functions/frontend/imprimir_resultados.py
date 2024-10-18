

def imprimir_ruta_menos_transbordos(origen , destino, camino, transbordos, estaciones_transbordo ):

    if camino:
        print(f"La ruta con menor cantidad de transbordos entre {origen} y {destino} es:")
        print(" -> ".join(camino))
        print(f"Número total de transbordos realizados: {transbordos}")
        if estaciones_transbordo:
            print(f"Transbordos realizados en las siguientes estaciones: {', '.join(estaciones_transbordo)}")
        else:
            print("No se realizaron transbordos.")
    else:
        print("No se encontró una ruta.")


def imprimir_ruta_corta(ruta, hora_llegada, tiempo_recorrido):
    
    
    print("hora de llegada: ", hora_llegada.time())
    print( "tiempo estimado de viaje",tiempo_recorrido)


    print("ruta de viaje: ", ruta)