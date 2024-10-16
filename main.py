#grafo de prueba
#from functions.pruebas.prueba_grafo                     import prueba_grafo
#muestra los resultados
#from functions.pruebas.prueba_grafo                     import mostrar
#ruta mas corta
from functions.algoritmos.dijkstra                      import dijkstra
#graficar
from functions.frontend.graficar_grafo                  import graficar_grafos
#grafo del metro
from functions.base_datos.grafo                         import grafo_metro
#busqueda en profundidad    
from functions.algoritmos.busqueda_profundidad          import Busqueda_profundidad
#cantidad de convinaciones en una ruta(idea no valida)
from functions.funcionalidades.cantidad_combinaciones   import cantidad_combinaciones
#convinaciones (array con que estaciones son convinaciones)
from functions.base_datos.combinaciones                 import combinaciones
#validar_datos
from functions.frontend.inicio_destino                  import input_usuario

#crea el grafo g con todas las lienas de metro y sus pesos
G = grafo_metro()


#indica un inicio y destino (despues esto debe ser cambiado al archivo inicio_destino)

#ruta mas corta entre origen y destino
#print("La ruta mas corta es:",dijkstra(G, origen, destino))

input_usuario()
