import heapq
import collections
import networkx as nx
from functions.base_datos.grafo import grafo_metro
from functions.base_datos  import combinaciones



def bfs_menor_transbordo(G, origen, destino):

    # Utilizamos una cola de prioridad para priorizar rutas con menos transbordos
    ruta = []  # Lista que actuará como cola de prioridad
    heapq.heappush(ruta, (0, [origen], None, [], 0))  # Añadido 0 al final para acumular tiempo total
    visitados = set()  # Cambiamos de diccionario a un set para que nos deje revisitar estaciones de combinacion por si son parte de una mejor ruta


    while ruta:  # Mientras no tengamos rutas vacías
        transbordos, camino, linea_actual, estaciones_transbordo, tiempo_acumulado = heapq.heappop(ruta)
        estacion_actual = camino[-1]  # La estación actual es la última estación del camino

        # Si la estación actual es igual al destino, retornamos los siguientes parámetros
        if estacion_actual == destino:
            return camino, transbordos, estaciones_transbordo, tiempo_acumulado

        if (estacion_actual, linea_actual, transbordos) in visitados:
            continue  # Evita explorar esta ruta si ya llegamos aquí con la misma línea y transbordos

        # Actualizamos el estado visitado con el número actual de transbordos
        visitados.add((estacion_actual, linea_actual, transbordos))

        # Explorar las estaciones vecinas
        for vecino in G.neighbors(estacion_actual):
            nueva_linea = G[estacion_actual][vecino]['linea']  # Determinamos la nueva línea
            nueva_ruta = list(camino)  # Hacemos una copia de la ruta actual
            nueva_estaciones_transbordo = list(estaciones_transbordo)
            nuevo_transbordo = transbordos
            nuevo_tiempo_acumulado = tiempo_acumulado + G[estacion_actual][vecino]['weight']  # Sumamos el tiempo de conexión

            # Si la línea actual es diferente de la nueva línea, es porque cambiamos de línea
            if linea_actual is not None and nueva_linea != linea_actual:
                nuevo_transbordo += 1  # Sumamos número de transbordos registrados
                nueva_estaciones_transbordo.append(estacion_actual)  # También registramos la estación donde se hizo el transbordo

            # Añadimos el vecino a la ruta
            nueva_ruta.append(vecino)

            # Siempre añadimos la ruta a la cola de prioridad para asegurar que se consideren todas las posibilidades
            heapq.heappush(ruta, (nuevo_transbordo, nueva_ruta, nueva_linea, nueva_estaciones_transbordo, nuevo_tiempo_acumulado))
            
    return None, None, [], None  # Si no se encontró una ruta