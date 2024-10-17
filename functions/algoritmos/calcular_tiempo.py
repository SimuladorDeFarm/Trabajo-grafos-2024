
#calcula cuanto se demora una ruta, recive un grafo networkx G
def calcular_tiempo(G, origen, destino):

    tiempo_total = nx.dijkstra_path_length(G, origen, destino, weight='weight')


    return tiempo_total


