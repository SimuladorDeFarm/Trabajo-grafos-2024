import collections
import networkx as nx
from functions.base_datos.grafo import grafo_metro

#Como no me quiere leer bien el archivo de combinaciones, añadí este trocito de codigo para que el sistema lo entienda bien.
def obtener_combinaciones(G):
    # Obtener estaciones con más de una línea
    combinaciones = set()
    for nodo in G.nodes():
        lineas_conectadas = set()
        for vecino in G.neighbors(nodo):
            lineas_conectadas.add(G[nodo][vecino]['linea'])
        if len(lineas_conectadas) > 1:
            combinaciones.add(nodo)
    
    #retorna un array de 1 dimension con las estaciones que pertenezcan a mas de una linea
    return combinaciones



def bfs_menor_transbordo(G, origen, destino):
    combinaciones = obtener_combinaciones(G)
    # Almacenamos las rutas posibles, empezando por la estación de origen
    ruta = collections.deque([([origen], 0, None, [], 0)])  # Añadido 0 al final para acumular tiempo total
    visitados = {}

    while ruta:  # Mientras no tengamos rutas vacías
        camino, transbordos, linea_actual, estaciones_transbordo, tiempo_acumulado = ruta.popleft()
        estacion_actual = camino[-1]  # La estación actual es la última estación del camino

        # Si la estación actual es igual al destino, retornamos los siguientes parámetros
        if estacion_actual == destino:
            return camino, transbordos, estaciones_transbordo, tiempo_acumulado

        # Aquí registramos las estaciones que ya visitamos (con su línea) para no revisitarlas
        if (estacion_actual, linea_actual) in visitados:
            if visitados[(estacion_actual, linea_actual)] <= transbordos:  # evitamos revisitar el mismo nodo con la misma línea y mismo número de transbordos
                continue

        # Actualizamos el estado visitado con el número actual de transbordos
        visitados[(estacion_actual, linea_actual)] = transbordos

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

            # Si la estación vecina no se visitó desde la misma línea o se llegó con un número menor de transbordos, se añade a la cola
            if (vecino, nueva_linea) not in visitados or visitados[(vecino, nueva_linea)] > nuevo_transbordo:
                ruta.append((nueva_ruta, nuevo_transbordo, nueva_linea, nueva_estaciones_transbordo, nuevo_tiempo_acumulado))

    return None, None, [], None  # Si no se encontró una ruta