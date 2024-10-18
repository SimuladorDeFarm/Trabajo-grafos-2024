import networkx as nx
from datetime import datetime, timedelta

#trasnforma time to datatime y recive una variable time
def transformar_time_to_datatime(time):
    hora_como_datetime = datetime.combine(datetime.today(), hora)

    return hora_como_datetime

def hora_actual():

    hora = datetime.now().time()
    
    return hora


#calcula cuanto se demora una ruta, recive un grafo networkx, y un origen y destino de tipo string
def calcular_tiempo(G, origen, destino):

    tiempo_total = nx.dijkstra_path_length(G, origen, destino, weight='weight')

    #retorna una variable de tipo int con el tiempo que demora la ruta
    return tiempo_total

#convierte minutos int a minutos en objeto timedelta
#recive variable int
def conversion_int_to_timedelta(tiempo_int):

    #trasnforma de int a hora
    minutos_a_sumar = timedelta(minutes=tiempo_int)

    #retorna una variable de tipo hora 
    return    minutos_a_sumar 

#suma los minutos que se demora la ruta a la hora entregada
#reecive la hora y los minutos que debe sumar, ambos de tipo time 
def sumar_minutos(hora, minutos_a_sumar):
    # Sumar el timedelta a la hora actual
    nueva_hora = hora + minutos_a_sumar

    #retorna variable tiempo con la hora a la que se llegara al destino
    return nueva_hora


#realzia todo el proceso de calcular la hora
def proceso_calcular_hora_llegada(G, origen, destino, hora):

    #tiempo que se demora una ruta, type = int     
    tiempo = calcular_tiempo(G, origen, destino)

    #transforma de int a timedelta
    tiempo_delta = conversion_int_to_timedelta(tiempo)

    #cnvierte hora (type = time) a timedelta
    hora_como_datetime = datetime.combine(datetime.today(), hora)
    
    #calcula hora de llegada segun la hora recivida y el tiempo de al ruta
    hora_llegada = sumar_minutos(hora_como_datetime, tiempo_delta)

    return hora_llegada, tiempo_delta
