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

#imprimir resultados finales
from functions.frontend.imprimir_resultados import imprimir_ruta_menos_transbordos, imprimir_ruta_corta

#limpiar pantalla
from functions.Os.funcionalidades_Os                               import    limpiar_pantalla

from datetime import datetime


#crea el grafo g con todas las lienas de metro y sus pesos
G = grafo_metro()

    
origen, destino, hora = input_usuario()

limpiar_pantalla()


hora_llegada, tiempo_recorrido = proceso_calcular_hora_llegada(G, origen, destino, hora)
ruta = dijkstra(G, origen, destino)


imprimir_ruta_corta(ruta, hora_llegada, tiempo_recorrido, origen, destino)



#Ruta menos transbordos


#parece que esto no se usa
combinaciones = obtener_combinaciones(G)

camino, transbordos, estaciones_transbordo, tiempo_recorrido_transbordos = bfs_menor_transbordo(G, origen, destino)



imprimir_ruta_menos_transbordos(origen, destino, camino, transbordos, estaciones_transbordo, tiempo_recorrido_transbordos)

'''
if __name__ == "__main__":
    combinaciones = obtener_combinaciones(G)
    # Buscar ruta con menor cantidad de transbordos
    camino, transbordos, estaciones_transbordo, tiempo_total = bfs_menor_transbordo(G, origen, destino)
    if camino:
        print(f"La ruta con menor cantidad de transbordos entre {origen} y {destino} es:")
        print(" -> ".join(camino))
        print(f"Número total de transbordos realizados: {transbordos}")
        if estaciones_transbordo:
            print(f"Transbordos realizados en las siguientes estaciones: {', '.join(estaciones_transbordo)}")
        else:
            print("No se realizaron transbordos.")
        print(f"Tiempo total del viaje: {tiempo_total} unidades de tiempo")
    else:
        print("No se encontró una ruta.")
'''