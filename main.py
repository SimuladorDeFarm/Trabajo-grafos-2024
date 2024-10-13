#grafo de prueba
from functions.prueba_grafo import prueba_grafo
#muestra los resultados
from functions.prueba_grafo import mostrar
#ruta mas corta
from functions.dijkstra     import ruta_mas_corta
#graficar
from functions.visual.graficar_grafo import graficar_grafos

G = prueba_grafo()
#mostrar(G)
#ruta_mas_corta(G, 1, 5)

#graficar grafo, (grafo, True = imprimir pesos, False = no imprimir pesos)
#graficar_grafos(G, False)

