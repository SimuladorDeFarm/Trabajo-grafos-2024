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
    ruta = collections.deque([([origen], 0, None, [])])
    visitados = {}
    while ruta:
        camino, transbordos, linea_actual, estaciones_transbordo = ruta.popleft()
        estacion_actual = camino[-1]
        if estacion_actual == destino:
            return camino, transbordos, estaciones_transbordo
        if (estacion_actual, linea_actual) in visitados:
            if visitados[(estacion_actual, linea_actual)] <= transbordos:
                continue
        visitados[(estacion_actual, linea_actual)] = transbordos
        for vecino in G.neighbors(estacion_actual):
            nueva_linea = G[estacion_actual][vecino]['linea']
            nueva_ruta = list(camino)
            nueva_estaciones_transbordo = list(estaciones_transbordo)
            nuevo_transbordo = transbordos
            if linea_actual is not None and nueva_linea != linea_actual:
                nuevo_transbordo += 1
                nueva_estaciones_transbordo.append(estacion_actual)
            nueva_ruta.append(vecino)
            if (vecino, nueva_linea) not in visitados or visitados[(vecino, nueva_linea)] > nuevo_transbordo:
                ruta.append((nueva_ruta, nuevo_transbordo, nueva_linea, nueva_estaciones_transbordo))

    return None, None, []