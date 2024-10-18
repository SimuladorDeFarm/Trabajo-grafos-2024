#grafo de prueba
#from functions.pruebas.prueba_grafo                     import prueba_grafo
#muestra los resultados
#from functions.pruebas.prueba_grafo                     import mostrar
#ruta mas corta
from functions.algoritmos.dijkstra                      import dijkstra
#graficar
from functions.frontend.graficar_grafo                                     import graficar_grafos
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

from functions.funcionalidades.ruta_menos_combinaciones import bfs_menor_transbordo
from functions.funcionalidades.ruta_menos_combinaciones import obtener_combinaciones

#calucula el tiempo entre dos estaciones
from functions.algoritmos.calcular_tiempo               import calcular_tiempo, hora_actual, conversion_int_to_timedelta, sumar_minutos, proceso_calcular_hora_llegada

from datetime import datetime


#crea el grafo g con todas las lienas de metro y sus pesos
G = grafo_metro()

    
origen, destino, hora = input_usuario()
hora_llegada, tiempo_recorrido = proceso_calcular_hora_llegada(G, origen, destino, hora)
ruta = dijkstra(G, origen, destino)


print("hora de llegada: ", hora_llegada.time())
print( "tiempo estimado de viaje",tiempo_recorrido)
print("ruta de viaje: ", ruta)


'''
#Ruta menos transbordos
if __name__ == "__main__":
    G = grafo_metro()
    
    #parece que esto no se usa
    combinaciones = obtener_combinaciones(G)
    
    origen = "hospitales"
    destino = "la granja"
    
    camino, transbordos, estaciones_transbordo = bfs_menor_transbordo(G, origen, destino)
    
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
'''