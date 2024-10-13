from functions.prueba_grafo import prueba_grafo
from functions.prueba_grafo import mostrar
from functions.dijkstra     import ruta_mas_corta

G = prueba_grafo()
#mostrar(G)
ruta_mas_corta(G, 1, 5)


