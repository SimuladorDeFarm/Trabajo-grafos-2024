import networkx as nx

def ruta_mas_corta(G, origen, destino):


    # Calcular la ruta más corta entre dos estaciones usando Dijkstra
    ruta_mas_corta = nx.dijkstra_path(G, origen, destino, weight='weight')  

    #print(ruta_mas_corta)
    return ruta_mas_corta