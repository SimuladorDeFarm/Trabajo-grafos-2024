import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt


def grafo_metro():
    # Cargar los datos desde el archivo CSV
    data = pd.read_csv('./functions/base_datos/metro_santiago.csv')

    # Crear un grafo vacío
    G = nx.Graph()

    # Añadir las conexiones entre estaciones con su respectivo tiempo
    for index, row in data.iterrows():
        G.add_edge(row['origen'], row['destino'], weight=row['tiempo'])

    #Verificar las estaciones y sus conexiones
    #print("Estaciones:", G.nodes())
    #print("Conexiones:", G.edges(data=True))

    return G







"""""
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

"""""
