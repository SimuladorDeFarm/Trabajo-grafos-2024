#grafo de prueba
from functions.prueba_grafo             import prueba_grafo
#muestra los resultados
from functions.prueba_grafo             import mostrar
#ruta mas corta
from functions.dijkstra                 import ruta_mas_corta
#graficar
from functions.visual.graficar_grafo    import graficar_grafos
#grafo del metro
from functions.grafo                    import grafo_metro
#busqueda en profundidad
from functions.ruta_menos_convinaciones import Busqueda_profundidad
#cantidad de convinaciones
from functions.cantidad_convinaciones   import cantidad_convinaciones
#convinaciones
from functions.convinaciones            import convinaciones

G = grafo_metro()

inicio = "plaza de puente alto"
destino = "tobalaba"


print(len(Busqueda_profundidad(G, inicio, destino)))
rutas_posibles = Busqueda_profundidad(G,  inicio, destino)


v =  convinaciones()

print(cantidad_convinaciones(rutas_posibles, v))




