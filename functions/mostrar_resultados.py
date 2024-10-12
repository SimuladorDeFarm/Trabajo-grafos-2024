import networkx as nx
from grafo import G


#Interaccion con usuario 
origen = str(input("Estacion origen: "))
destino = str(input("Estacion destino: "))

# Calcular la ruta más corta entre dos estaciones usando Dijkstra
ruta_mas_corta = nx.dijkstra_path(G, origen, destino, weight='weight')
tiempo_total = nx.dijkstra_path_length(G, origen, destino, weight='weight')
hora = 0

if tiempo_total <= 60:
    print(f"La ruta mas corta entre {origen} y {destino} es alrededor de {tiempo_total} minuto/s")
else:
     tiempo_total = tiempo_total / 6 
     tiempo_total_redondeado = round(tiempo_total, 0)
     hora += 1
     print(f"La ruta mas corta entre {origen} y {destino} es alrededor de {hora} hora/s y {tiempo_total_redondeado} minuto/s")
#end if  
