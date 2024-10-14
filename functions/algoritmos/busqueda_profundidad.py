import networkx as nx


def Busqueda_profundidad(G, inicio, destino):

    rutas = list(nx.all_simple_paths(G, inicio, destino))

    #for ruta in rutas:
     #   print(f"Ruta: {ruta}")

    return rutas