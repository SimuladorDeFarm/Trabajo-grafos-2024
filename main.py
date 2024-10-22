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


#calucula el tiempo entre dos estaciones
from functions.algoritmos.calcular_tiempo               import calcular_tiempo, hora_actual, conversion_int_to_timedelta, sumar_minutos, proceso_calcular_hora_llegada, proceso_calcular_hora_llegada_transbordos

#imprimir resultados finales
from functions.frontend.imprimir_resultados import imprimir_ruta_menos_transbordos, imprimir_ruta_corta

from functions.frontend.lista_estaciones_metro      import estacion_linea


#limpiar pantalla
from functions.Os.funcionalidades_Os                               import    limpiar_pantalla

from datetime import datetime


def  menu():
        #crea el grafo g con todas las lienas de metro y sus pesos
    G = grafo_metro()

    #obtiene el origen, destino y hora programa (o actual) del ususario 
    origen, destino, hora = input_usuario()

    #limpia la pantalla para mostrar los resultados
    limpiar_pantalla()

    #Calculla la hora de llegada 
    hora_llegada, tiempo_recorrido = proceso_calcular_hora_llegada(G, origen, destino, hora)

    #calcula la ruta mas corta
    ruta = dijkstra(G, origen, destino)

    #imprime los resultados de la ruta corta
    imprimir_ruta_corta(ruta, hora_llegada, tiempo_recorrido, origen, destino, hora)



    #Ruta menos transbordos

    #cacula la ruta con menos transbordos
    #camani, transbordos y estaciones_transbordos son arrays con strings
    #tiempo_recorido_transborods es de tipo entero
    camino, transbordos, estaciones_transbordo, tiempo_recorrido_transbordos = bfs_menor_transbordo(G, origen, destino)

    hora_llegada_transbordos, tiempo_recorrido_transbordos = proceso_calcular_hora_llegada_transbordos(hora, tiempo_recorrido_transbordos)

    imprimir_ruta_menos_transbordos(origen, destino, camino, transbordos, estaciones_transbordo, tiempo_recorrido_transbordos, hora_llegada_transbordos, hora)

    

menu()